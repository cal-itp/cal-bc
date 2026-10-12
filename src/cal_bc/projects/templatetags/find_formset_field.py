from django import template

register = template.Library()


@register.filter
def find_formset_field(formset, field):
    for form in formset:
        if hasattr(form, "initial") and "field" in form.initial and form.initial["field"] == field or hasattr(form, "instance") and hasattr(form.instance, "field") and form.instance.field == field:
            return form

@register.filter
def find_project_field(project, field):
    for value in project.input_set.all():
        if hasattr(value, "field") and value.field == field:
            return value
    for value in project.calculation_set.all():
        if hasattr(value, "field") and value.field == field:
            return value

@register.filter
def find_fieldset_row(field_set, row):
    for field in field_set:
        if hasattr(field, "row") and field.row == row:
            return field

@register.filter
def find_formset_row_errors(formset, row):
    errors = []
    for form in formset:
        if hasattr(form, "instance") and hasattr(form.instance, "field") and form.instance.field.row == row:
            for form_errors in form.errors.values():
                for form_error in form_errors:
                    if form_error not in errors:
                        errors.append(form_error)
    if errors:
        return ", ".join(item.replace(".", "") for item in errors) + '.'
    return ""
