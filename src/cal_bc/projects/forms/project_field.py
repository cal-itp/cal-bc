from django.forms import ModelForm
from cal_bc.projects.models.project_field import ProjectField
from django.utils.translation import gettext as _


class ProjectFieldForm(ModelForm):
    class Meta:
        model = ProjectField
        fields = ["value", "project"]
        labels = {"value": _("Value")}
        widgets = {"project": Hidden()}

        def get_labels(self) -> dict[str, str]:
            return {"value": _(self.object.model_section_field.name)}


ProjectFieldFormset = inlineformset_factory(
    ModelSectionField, ProjectField, form=ProjectFieldForm, allow_create=False
)
