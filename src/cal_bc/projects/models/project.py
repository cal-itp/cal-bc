from django.contrib.auth.models import User
from django.db import models, transaction

from cal_bc.models.models.model import Field, Version


class Project(models.Model):
    version = models.ForeignKey(
        Version, null=False, db_index=True, on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, null=False, db_index=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self) -> str:
        return self.name.value if self.name and self.name.value else "New Project"

    @property
    def name(self):
        return self.value_set.filter(field__name="Project Name").first()


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

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "project",
                    "field",
                ],
                name="unique_project_field",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.field!s} {self.value}"

    def save(self, *args, **kwargs):
        with transaction.atomic():
            super().save(*args, **kwargs)
            transaction.on_commit(self.project.save)
