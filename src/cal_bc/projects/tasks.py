from io import BytesIO
import logging
import urllib.request
from cal_bc.models.models.model import Field
from cal_bc.projects.models.project import Project
from cal_bc_calculator.calculator import Calculator
from django.tasks import task


logger = logging.getLogger(__name__)

@task
def refresh_project_fields(project_pk: int) -> None:
    project = Project.objects.get(id=project_pk)
    value_cells = {v.field.cell: v.value for v in project.value_set.all()}
    field_set = Field.objects.filter(
        row__group__subsection__section__version=project.version
    )
    req = urllib.request.Request(project.version.url)
    resp = urllib.request.urlopen(req)
    calculator = Calculator(BytesIO(resp.read()))
    calculator.write(value_cells)
    compiled = calculator.compile()
    for field in field_set.all():
        value = compiled.evaluate(field.cell)
        project_value, created = project.value_set.get_or_create(
            field=field,
            defaults={"value": value}
        )
        if not created:
            project_value.save()
