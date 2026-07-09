from django.forms import ModelForm, ChoiceField, CharField, HiddenInput
from cal_bc.projects.models.project import Value
from django.utils.translation import gettext as _

class ValueForm(ModelForm):
    class Meta:
        model = Value
        fields = ['value', 'field']

        labels = {
            "value": _("Value"),
            "field": _("Field"),
        }

        widgets = {
            "field": HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'initial' in kwargs:
            field = kwargs['initial']['field']
        if 'instance' in kwargs:
            field = kwargs['instance'].field
        values = field.value_set.all()
        if len(values):
            self.fields['value'] = ChoiceField(
                choices=[(None, ""), *[(v.value, v.name) for v in values]]
            )
        else:
            self.fields['value'] = CharField()
        self.fields['value'].label = field.name
