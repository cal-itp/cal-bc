from django.forms import ModelForm
from cal_bc.projects.models.model_section import ModelSection
from django.utils.translation import gettext as _


class ModelSectionForm(ModelForm):
    class Meta:
        model = ModelSection
        fields = ["section_fields"]

        def get_labels(self) -> dict[str, str]:
            return {"section_fields": _(self.object.name)}
