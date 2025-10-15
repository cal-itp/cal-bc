from django.forms import ModelForm
from cal_bc.projects.models.project import Project
from django.utils.translation import gettext as _


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "district",
            "type",
            "location",
            "construction_period_length",
            "data_direction",
            "peak_periods_length",
        ]

        labels = {
            "name": _("Project Name"),
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
