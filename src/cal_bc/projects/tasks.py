import logging
import urllib.request
from functools import partial
from io import BytesIO

from django.db import transaction
from django.tasks import task

from cal_bc.models.models.model import Field, Subsection
from cal_bc.projects.models.project import Project, Value
from cal_bc.tasks import refresh_channel
from cal_bc_calculator.calculator import Calculator

logger = logging.getLogger(__name__)

@task
def refresh_project_fields(project_pk: int) -> None:
    project = Project.objects.get(id=project_pk)
    cell_values = {v.field.cell: v.value for v in project.value_set.exclude(field__cell="").exclude(value="")}
    field_set = Field.objects.filter(row__group__subsection__section__version=project.version).exclude(cell="")
    req = urllib.request.Request(project.version.url)
    resp = urllib.request.urlopen(req)
    calculator = Calculator(BytesIO(resp.read()))
    compiled = calculator.compile()
    for cell, value in cell_values.items():
        compiled.set_cell_value(cell, value)
    with transaction.atomic():
        value_set = [Value(project=project, field=f, value=compiled.evaluate(f.cell)) for f in field_set.all()]
        Value.objects.bulk_create(value_set, update_conflicts=True, update_fields=("value",), unique_fields=("project", "field"))
        transaction.on_commit(partial(refresh_channel.enqueue, channel_name=f"user_{project.user_id}_projects"))
        for subsection in Subsection.objects.filter(section__version__project=project):
            transaction.on_commit(partial(refresh_channel.enqueue, channel_name=f"project_{project.pk}_subsection_{subsection.pk}"))
