from django.db import models
from cal_bc.models.models.model import Version, Field, Row, Group, Subsection, Section
from django.contrib.auth.models import User


class Project(models.Model):
    version = models.ForeignKey(
        Version, null=False, db_index=True, on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, null=False, db_index=True, on_delete=models.CASCADE
    )

    def name_value(self):
        return self.value_set.filter(
            field_id__in=Field.objects.filter(
                name="Project Name",
                row_id__in=Row.objects.filter(
                    group_id__in=Group.objects.filter(
                        subsection_id__in=Subsection.objects.filter(
                            section_id__in=Section.objects.filter(
                                version_id=self.version_id
                            ).all()
                        ).all()
                    ).all()
                ).all()
            ).all()
        ).first()

    def __str__(self) -> str:
        name_value = self.name_value()
        return name_value.value if name_value else "New Project"


class Value(models.Model):
    project = models.ForeignKey(
        Project, null=False, db_index=True, on_delete=models.CASCADE
    )
    field = models.ForeignKey(
        Field, null=False, db_index=True, related_name="project_value_set", on_delete=models.CASCADE
    )
    value = models.CharField(null=False)
