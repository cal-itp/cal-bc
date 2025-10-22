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
            "model_version",
            "district",
            "type",
            "location",
            "construction_period_length",
            "data_direction",
            "peak_periods_length",
        ]

        labels = {
            "name": _("Project Name"),
            "model_version": _("Model Version"),
            "type": _("Project Type"),
            "location": _("Project Location"),
            "construction_period_length": _("Length of Construction Period"),
            "data_direction": _("One- or Two-Way Data"),
            "peak_periods_length": _("Length of Peak Period(s) (up to 24 hrs)"),
        }

        help_texts = {
            "construction_period_length": _("years"),
            "peak_periods_length": _("hours"),
        }
