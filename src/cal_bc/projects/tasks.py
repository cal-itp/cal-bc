import logging
import urllib.request
from functools import partial
from io import BytesIO

from django.db import transaction
from django.tasks import task

from cal_bc.models.models.model import Field
from cal_bc.projects.models.project import Project
from cal_bc.tasks import refresh_channel
from cal_bc_calculator.calculator import Calculator

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
    changed_subsections = set()
    with transaction.atomic():
        for field in field_set.all():
            value = compiled.evaluate(field.cell)
            project_value, created = project.value_set.get_or_create(
                field=field,
                defaults={"value": value}
            )
            if not created and project_value.value != value_cells[project_value.field.cell]:
                project_value.value = value
                project_value.save()
            if created or project_value.value != value_cells[project_value.field.cell]:
                changed_subsections.add(project_value.field.row.group.subsection)
        for subsection in changed_subsections:
            transaction.on_commit(partial(refresh_channel.enqueue, channel_name=f"user_{project.user_id}_project_{project.pk}_subsection_{subsection.pk}"))
        if len(changed_subsections) > 0:
            transaction.on_commit(partial(refresh_channel.enqueue, channel_name=f"user_{project.user_id}_projects"))
