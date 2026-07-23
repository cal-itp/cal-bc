from django.contrib.auth.models import User
from django.db import models

from cal_bc.models.models.model import Field, Version


class Project(models.Model):
    class Meta:
        ordering = ["-updated_at"]

    version = models.ForeignKey(
        Version, null=False, db_index=True, on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, null=False, db_index=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def name_value(self):
        return self.value_set.filter(
            field__name="Project Name",
            field__row__group__subsection__section__version=self.version,
        ).first()

    def __str__(self) -> str:
        name_value = self.name_value()
        return name_value.value if name_value else "New Project"


class Value(models.Model):
    project = models.ForeignKey(
        Project, null=False, db_index=True, on_delete=models.CASCADE
    )
    field = models.ForeignKey(
        Field,
        null=False,
        db_index=True,
        related_name="project_value",
        on_delete=models.CASCADE,
    )
    value = models.CharField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.project.save()
