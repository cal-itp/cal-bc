from django.contrib.auth.models import User
from django.db import models, transaction
from django.tasks.base import TaskResultStatus
from django_tasks_db.models import DBTaskResult

from cal_bc.models.models.model import Field, Version

class ProjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().fetch_mode(models.FETCH_RAISE)

class Project(models.Model):
    version = models.ForeignKey(
        Version, null=False, db_index=True, on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, null=False, db_index=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    objects = ProjectManager()

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self) -> str:
        return self.name.value if self.name and self.name.value else "New Project"

    @property
    def name(self):
        if hasattr(self, "project_names"):
            names = self.project_names
        else:
            names = self.value_set.project_names()

        return names[0] if len(names) else {}


    @property
    def benefit_cost_ratio(self):
        return self.value_set.filter(field__name="Benefit / Cost Ratio").first()

    @property
    def summary_value_set(self):
        return self.value_set.filter(field__row__group__is_summary=True).all()


class ValueManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().fetch_mode(models.FETCH_RAISE)

    def project_names(self):
        return self.filter(field__name="Project Name")


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

    objects = ValueManager()

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
        return self.value

    def save(self, *args, **kwargs):
        with transaction.atomic():
            super().save(*args, **kwargs)
            transaction.on_commit(self.project.save)


class RefreshTaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().fetch_mode(models.FETCH_RAISE)

    def active(self):
      return self.filter(db_task_result__status=TaskResultStatus.READY) | self.filter(db_task_result__status=TaskResultStatus.RUNNING)


class RefreshTask(models.Model):
    project = models.ForeignKey(
        Project, null=False, db_index=True, on_delete=models.CASCADE
    )
    db_task_result = models.ForeignKey(
        DBTaskResult, null=False, db_index=True, on_delete=models.CASCADE
    )

    objects = RefreshTaskManager()

    def __str__(self) -> None:
        return f"RefreshTask #{self.id}"
