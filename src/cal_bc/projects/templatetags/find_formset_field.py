from django import template

register = template.Library()


@register.filter
def find_formset_field(formset, field):
    for form in formset:
        if hasattr(form, "initial") and "field" in form.initial and form.initial["field"] == field or hasattr(form, "instance") and hasattr(form.instance, "field") and form.instance.field == field:
            return form

@register.filter
def find_valueset_field(value_set, field):
    for value in value_set:
        if hasattr(value, "field") and value.field == field:
            return value

@register.filter
def find_fieldset_row(field_set, row):
    for field in field_set:
        if hasattr(field, "row") and field.row == row:
                return field
