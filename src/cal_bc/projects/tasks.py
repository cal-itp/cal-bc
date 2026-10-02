import logging
from functools import cached_property, partial

from django.db import transaction
from django.tasks import task

from cal_bc.models.models.model import (
    Field,
    FieldDisplayType,
    Subsection,
)
from cal_bc.projects.models.project import Project, Value
from cal_bc.tasks import refresh_channel
from cal_bc_calculator.calculator import BytesCalculator
from cal_bc_calculator.downloader import Downloader

logger = logging.getLogger(__name__)


class RemoteWorkbook:
    def __init__(self, url: str) -> None:
        self.url = url

    @property
    def downloader(self) -> Downloader:
        return Downloader(url=self.url)

    @cached_property
    def calculator(self) -> BytesCalculator:
        return BytesCalculator(self.downloader.to_bytes())

    def set_cell_values(self, cell_values: dict[str, any]) -> None:
        self.calculator.write(cell_values)

    def read_cell_values(self, cells: list[str]) -> dict[str, any]:
        return {k: v for k, v in zip(cells, self.calculator.evaluate(cells))}

def coerce_value(value: any) -> any:
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value

@task
def refresh_project_fields(project_pk: int) -> None:
    project = Project.objects.get(id=project_pk)

    remote_workbook = RemoteWorkbook(url=project.version.url)
    cell_values = {
        value.field.cell: coerce_value(value.value)
        for value in project.value_set.exclude(field__cell="").exclude(value="").exclude(field__display_type=FieldDisplayType.READ_ONLY).exclude(field__row__group__is_summary=True).select_related("field")
    }
    remote_workbook.set_cell_values(cell_values)
    field_set = Field.objects.filter(row__group__subsection__section__version=project.version).exclude(cell="")
    calculated_values = remote_workbook.read_cell_values([f.cell for f in field_set.all()])
    value_set = [Value(project=project, field=f, value=calculated_values[f.cell]) for f in field_set.all() if calculated_values[f.cell] is not None]

    with transaction.atomic():
        Value.objects.bulk_create(value_set, update_conflicts=True, update_fields=("value",), unique_fields=("project", "field"))

        transaction.on_commit(partial(refresh_channel.enqueue, channel_name=f"user_{project.user_id}_projects"))

        for subsection in Subsection.objects.filter(section__version__project=project):
            transaction.on_commit(partial(refresh_channel.enqueue, channel_name=f"project_{project.pk}_subsection_{subsection.pk}"))
