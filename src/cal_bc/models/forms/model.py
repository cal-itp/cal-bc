from django.forms import ModelForm
from django.utils.translation import gettext as _

from cal_bc.projects.models.project import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["version", "user"]

        labels = {
            "version": _("Model Version"),
            "user": _("User"),
        }
