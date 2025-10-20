from django.forms import ModelForm
from cal_bc.projects.models.project import Project
from django.utils.translation import gettext as _


class ProjectForm(ModelForm):
    def __init__(self, disable_fields=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if disable_fields:
            for field in self.fields:
                self.fields[field].disabled = True

    class Meta:
        model = Project
        fields = [
            "name",
            "district",
            "model",
        ]

        labels = {
            "name": _("Project Name"),
            "model": _("Model"),
            "district": _("District"),
        }
