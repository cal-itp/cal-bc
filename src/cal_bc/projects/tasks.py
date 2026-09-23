import formualizer
from itertools import groupby
import formualizer
import logging
import urllib.request
from functools import cached_property, partial
from io import BytesIO

from django.db import transaction
from django.tasks import task
from xlcalculator import Evaluator, Model, ModelCompiler, xltypes

from cal_bc.models.models.model import Field, FieldDisplayType, Subsection
from cal_bc.projects.models.project import Project, Value
from cal_bc.tasks import refresh_channel

logger = logging.getLogger(__name__)


class RemoteWorkbook:
    def __init__(self, url: str) -> None:
        self.url = url

    @property
    def request(self) -> urllib.request.Request:
        return urllib.request.Request(self.url)

    @cached_property
    def workbook_bytes(self) -> bytes:
        return urllib.request.urlopen(self.request).read()

    @cached_property
    def workbook(self) -> formualizer.Workbook:
        return formualizer.load_workbook_bytes(self.workbook_bytes, backend="umya")

    @property
    def defined_names(self) -> dict[str, tuple[str, int, int]]:
        return {
            nr['name']: (nr["sheet"], nr["start_row"], nr["start_col"])
            for nr in self.workbook.get_named_ranges() if nr["kind"] == "cell"
        }

    def resolve_address(self, address: str) -> tuple[str, int, int]:
        def excel_column_index(column):
            n = 0
            for char in column:
                n = n * 26 + 1 + ord(char) - ord('A')
            return n

        if address in self.defined_names:
            return self.defined_names[address]
        else:
            sheet, cell = address.split("!")
            column, row = ["".join(g) for _, g in groupby(cell, str.isalpha)]
            return (sheet, int(row), excel_column_index(column))

    def evaluate(self, address: str) -> any:
        return self.workbook.evaluate_cell(*self.resolve_address(address))

    def set_cell_value(self, address: str, value: str) -> None:
        return self.workbook.set_value(*self.resolve_address(address), value)

@task
def refresh_project_fields(project_pk: int) -> None:
    project = Project.objects.get(id=project_pk)

    remote_workbook = RemoteWorkbook(url=project.version.url)
    for value in project.value_set.exclude(field__cell="").exclude(value="").exclude(field__display_type=FieldDisplayType.READ_ONLY).exclude(field__row__group__is_summary=True).select_related("field"):
        try:
            remote_workbook.set_cell_value(address=value.field.cell, value=value.value)
        except ValueError as e:
            logger.error(f"Cannot set {value.field.cell} to {value.value}: {e}")
            raise

    field_set = Field.objects.filter(row__group__subsection__section__version=project.version).exclude(cell="")
    value_set = [Value(project=project, field=f, value=remote_workbook.evaluate(f.cell)) for f in field_set.all()]

    with transaction.atomic():
        Value.objects.bulk_create(value_set, update_conflicts=True, update_fields=("value",), unique_fields=("project", "field"))

        transaction.on_commit(partial(refresh_channel.enqueue, channel_name=f"user_{project.user_id}_projects"))

        for subsection in Subsection.objects.filter(section__version__project=project):
            transaction.on_commit(partial(refresh_channel.enqueue, channel_name=f"project_{project.pk}_subsection_{subsection.pk}"))
