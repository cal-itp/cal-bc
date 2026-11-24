import re

from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.translation import gettext as _

from cal_bc.models.models.model import Choice, Subsection
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


class FieldForm(ModelForm):
    def clean_cell(self):
        subsection = Subsection.objects.get(id=self.data.get('subsection'))
        if subsection and not hasattr(subsection.section.version, "versionfile"):
            raise ValidationError("No Workbook found. Please go to Version page, click on Save to download the file.")

        version_file = subsection.section.version.versionfile
        cell_value = self.cleaned_data.get("cell")

        match cell_value.count("!"):
            case 0:
                if not version_file.versionfilenamedcell_set.exists():
                    raise ValidationError("No Named Cells found. Please go to Version page, click on Save to load the file details.")
                
                if cell_value not in list(version_file.versionfilenamedcell_set.all().values_list('name', flat=True)):
                    raise ValidationError("Invalid Named Cell.")
            case 1:
                if not version_file.versionfilesheet_set.exists():
                    raise ValidationError("No Sheet Names found. Please go to Version page, click on Save to load the file details.")
                
                sheet, cell = cell_value.split("!")
                if sheet not in list(version_file.versionfilesheet_set.all().values_list('name', flat=True)):
                   raise ValidationError("Invalid Sheet Name. Check the name you entered before the exclamation point.")
                if not bool(re.match(r"^[A-Za-z]+\d+$", cell)):
                    raise ValidationError("Invalid Column and Row definition. Check the value you entered after the exclamation point.")
            case _:
                raise ValidationError("Only one exclamation point is allowed in the cell address.")
        
        return cell_value
