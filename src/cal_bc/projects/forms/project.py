from django.core.exceptions import ValidationError
from django.forms import CharField, ChoiceField, DecimalField, HiddenInput, ModelForm
from django.utils.translation import gettext as _

from cal_bc.projects.models.project import Input


class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = ["value", "field"]

        labels = {
            "value": _("Value"),
            "field": _("Field"),
        }

        widgets = {
            "field": HiddenInput(),
        }

    def clean_value(self):
        value = self.cleaned_data.get("value")
        if hasattr(self.instance, "field") and self.instance.field.read_only:
            return self.instance.value
        if value and hasattr(self.instance, "field") and hasattr(self.instance.field, "fieldrange") and not (self.instance.field.fieldrange.min_value <= float(value) <= self.instance.field.fieldrange.max_value):
            raise ValidationError(f"Enter a number between {self.instance.field.fieldrange.min_value} and {self.instance.field.fieldrange.max_value} on {self.instance.field.name}.")
        return value

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field = None

        if "initial" in kwargs:
            field = kwargs["initial"]["field"]

        if "instance" in kwargs:
            field = kwargs["instance"].field

        if field:
            choices = field.choice_set.all()

            if len(choices):
                self.fields["value"] = ChoiceField(
                    choices=[(None, ""), *[(i.value, i.name) for i in choices]],
                    required=field.required,
                    error_messages={"required": f"Select {field.name}."},
                )
            elif hasattr(field, "fieldrange") or field.unit:
                self.fields["value"] = DecimalField(required=field.required, error_messages={"required": f"Enter {field.name}."})
            else:
                self.fields["value"] = CharField(required=field.required, error_messages={"required": f"Enter {field.name}."})

            self.fields["value"].label = field.name
