from django.db import models


class Model(models.Model):
    name = models.CharField(null=False)
    url = models.CharField(null=False)

    def __str__(self):
        return self.name
