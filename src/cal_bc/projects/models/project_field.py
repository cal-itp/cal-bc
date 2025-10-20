from django.db import models

from .model_section_field import ModelSectionField
from .project import Project


class ProjectField(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="fields", null=False
    )
    model_section_field = models.ForeignKey(
        ModelSectionField,
        on_delete=models.CASCADE,
        related_name="project_fields",
        null=False,
    )
    value = models.CharField(null=False)

    def __str__(self):
        return self.value
