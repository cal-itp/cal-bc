from django.db import models


class ModelVersion(models.Model):
    name = models.CharField(null=False)
    version = models.CharField(null=False)
    url = models.CharField(null=False)

    def __str__(self):
        return f"{self.name} v{self.version}"
