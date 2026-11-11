from django.core.exceptions import ValidationError
from django.forms import CharField, ChoiceField, DecimalField, HiddenInput, ModelForm, FloatField, TextInput
from django.utils.translation import gettext as _

from cal_bc.projects.models.project import Input


def is_number(value):
    if value is None:
        return False
    try:
        float(value)
        return True
    except ValueError:
        return False


class PercentageField(FloatField):
    def to_python(self, value):
        val = super(PercentageField, self).to_python(value)
        if is_number(val):
            return val/100
        return val

    def prepare_value(self, value):
        val = super(PercentageField, self).prepare_value(value)
        if is_number(val):
            return str((float(val)*100))
        return val


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

        if value is None:
            value = ""

        if self.field.read_only:
            return self.instance.value

        if value is not "" and hasattr(self.field, "fieldrange") and not (self.field.fieldrange.min_value <= float(value) <= self.field.fieldrange.max_value):
            min_value_display = self.field.fieldrange.min_value * 100 if self.is_percentage else self.field.fieldrange.min_value
            max_value_display = self.field.fieldrange.max_value * 100 if self.is_percentage else self.field.fieldrange.max_value
            raise ValidationError(f"Enter a number between {min_value_display} and {max_value_display} on {self.field.name}.")

        return value

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field = None

        if "initial" in kwargs:
            self.field = kwargs["initial"]["field"]

        if "instance" in kwargs:
            self.field = kwargs["instance"].field

        assert self.field is not None

        self.is_percentage = self.field.unit == "%"
        field_class = CharField
        field_class_config = {"required": self.field.required, "error_messages": {'required': f'Enter {self.field.name}.'}}
        choices = self.field.choice_set.all()

        if len(choices):
            field_class = ChoiceField
            field_class_config["choices"] = [(None, ""), *[(i.value, i.name) for i in choices]]
            field_class_config["error_messages"] = {'required': f'Select {self.field.name}.'}
        elif self.is_percentage:
            field_class = PercentageField
        elif hasattr(self.field, "fieldrange") or self.field.unit:
            field_class = DecimalField

        self.fields["value"] = field_class(**field_class_config)
        self.fields["value"].label = self.field.name
