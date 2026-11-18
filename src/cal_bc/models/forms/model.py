import re

from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.translation import gettext as _

from cal_bc.models.models.model import Choice, VersionFileNamedCell, VersionFileSheet
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
        cell_address = self.cleaned_data.get("cell")
        delimiter = cell_address.count("!")
        
        match delimiter:
            case 0:
                named_cells = list(VersionFileNamedCell.objects.filter(version_file=self.instance.row.group.subsection.section.version.versionfile).values_list('name', flat=True))
                if cell_address not in named_cells:
                    raise ValidationError("Invalid named cell.")
            case 1:
                sheet, cell = cell_address.split("!")
                sheet_names = list(VersionFileSheet.objects.filter(version_file=self.instance.row.group.subsection.section.version.versionfile).values_list('name', flat=True))
                
                if sheet not in sheet_names:
                    raise ValidationError("Invalid sheet name. Check the name you entered before the exclamation point.")
                if not bool(re.match(r"^[A-Za-z]+\d+$", cell)):
                    raise ValidationError("Invalid row and column definition. Check the value you entered after the exclamation point.")
            case _ if delimiter > 1:
                raise ValidationError("Only one exclamation point is allowed in a cell address.")
        
        return cell_address
