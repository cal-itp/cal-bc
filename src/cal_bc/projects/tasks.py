import logging
import urllib.request
from functools import cached_property, partial
from io import BytesIO

from django.db import transaction
from django.tasks import task
from xlcalculator import Evaluator, Model, ModelCompiler, xltypes

from cal_bc.models.models.model import Field, Subsection
from cal_bc.projects.models.project import Project, Value
from cal_bc.tasks import refresh_channel

logger = logging.getLogger(__name__)

class RemoteWorkbook:
    def __init__(self, url: str) -> None:
        self.url = url

    @cached_property
    def request(self) -> urllib.request.Request:
        return urllib.request.Request(self.url)

    @cached_property
    def workbook(self) -> BytesIO:
        return BytesIO(urllib.request.urlopen(self.request).read())

    @cached_property
    def evaluator(self) -> Evaluator:
        compiler: ModelCompiler = ModelCompiler()
        model: Model = compiler.read_and_parse_archive(self.workbook, build_code=True)
        return Evaluator(model)

    def evaluate(self, address: str) -> any:
        return self.evaluator.evaluate(address)

    def set_cell_value(self, address: str, value: str) -> None:
        self.evaluator.set_cell_value(address=address, value=value)

        addr = self.evaluator.resolve_names(address)
        if addr in self.evaluator.model.defined_names and isinstance(self.evaluator.model.defined_names[addr], xltypes.XLCell):
                addr = self.evaluator.model.defined_names[addr].address

        if isinstance(addr, str):
            self.evaluator.model.cells[addr].formula = None

        elif isinstance(addr, xltypes.XLCell):
            self.evaluator.model.cells[addr.address].formula = None


@task
def refresh_project_fields(project_pk: int) -> None:
    project = Project.objects.get(id=project_pk)

    remote_workbook = RemoteWorkbook(url=project.version.url)

    for value in project.value_set.exclude(field__cell="").exclude(value="").exclude(field__read_only=True).select_related("field"):
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
