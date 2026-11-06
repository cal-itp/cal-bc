from django.forms import ModelForm
from django.utils.translation import gettext as _

from cal_bc.models.models.model import Choice
from cal_bc.projects.models.project import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["version", "user"]

        labels = {
            "version": _("Model Version"),
            "user": _("User"),
        }

class ChoiceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['value'].strip = False

    class Meta:
        model = Choice
        fields = ["name", "value", "is_selected", "position"]
