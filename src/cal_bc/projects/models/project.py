from django.db import models


class Project(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name
