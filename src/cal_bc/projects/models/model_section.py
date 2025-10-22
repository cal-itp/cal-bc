from django.db import models

from .model import Model


class ModelSection(models.Model):
    name = models.CharField(null=False)
    help_text = models.CharField(null=False)
    model = models.ForeignKey(
        Model, on_delete=models.CASCADE, related_name="sections", null=False
    )

    def __str__(self):
        return self.name
