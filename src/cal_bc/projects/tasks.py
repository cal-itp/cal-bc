import logging
from functools import cached_property, partial

from django.core.files import File
from django.db import transaction
from django.tasks import task

from cal_bc.models.models.model import (
    Field,
    Subsection,
    Version,
)
from cal_bc.models.tasks import refresh_version_file
from cal_bc.projects.models.project import Calculation, Project
from cal_bc.tasks import refresh_channel
from cal_bc_calculator.calculator import BytesCalculator

logger = logging.getLogger(__name__)


class RemoteWorkbook:
    def __init__(self, version: Version) -> None:
        self.version = version

    @cached_property
    def file(self) -> File:
        if not hasattr(self.version, "versionfile"):
            refresh_version_file.func(version_pk=self.version.pk)
            self.version.refresh_from_db()
        with self.version.versionfile.file.open() as f:
            return f.read()

    @cached_property
    def calculator(self) -> BytesCalculator:
        return BytesCalculator(self.file)

    def set_cell_values(self, cell_values: dict[str, any]) -> None:
        self.calculator.write(cell_values)

    def read_cell_values(self, cells: list[str]) -> dict[str, any]:
        return {k: v for k, v in zip(cells, self.calculator.evaluate(cells))}


@task
def refresh_project_fields(project_pk: int) -> None:
    project = Project.objects.select_related('version').get(id=project_pk)

    remote_workbook = RemoteWorkbook(version=project.version)
    cell_values = {
        input.field.cell: input.value
        for input in project.input_set.exclude(field__cell="").exclude(value="").select_related("field")
    }
    remote_workbook.set_cell_values(cell_values)
    field_set = Field.objects.filter(row__group__subsection__section__version=project.version).exclude(cell="")
    calculated_values = remote_workbook.read_cell_values([f.cell for f in field_set.all()])
    calculation_set = [
        Calculation(project=project, field=f, value=calculated_values[f.cell])
        for f in field_set.all()
        if calculated_values[f.cell] is not None
    ]

    with transaction.atomic():
        Calculation.objects.bulk_create(calculation_set, update_conflicts=True, update_fields=("value",), unique_fields=("project", "field"))

        transaction.on_commit(partial(refresh_channel.enqueue, channel_name=f"user_{project.user_id}_projects"))
        for subsection in Subsection.objects.filter(section__version__project=project):
            transaction.on_commit(partial(refresh_channel.enqueue, channel_name=f"project_{project.pk}_subsection_{subsection.pk}"))
