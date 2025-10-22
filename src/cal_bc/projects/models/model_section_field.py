from django.db import models

from .model_section import ModelSection


class ModelSectionField(models.Model):
    name = models.CharField(null=False)
    cell = models.CharField(null=False)
    help_text = models.CharField(null=False)
    section = models.ForeignKey(
        ModelSection,
        on_delete=models.CASCADE,
        related_name="section_fields",
        null=False,
    )

    def __str__(self):
        return self.name
