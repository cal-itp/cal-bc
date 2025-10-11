from django.forms import ModelForm
from cal_bc.projects.models.project import Project
from django.utils.translation import gettext as _


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["name"]
        labels = {"name": _("Project name")}
