from decimal import Decimal

from django import template

register = template.Library()

def is_number(value):
    if value is None:
        return False
    try:
        float(value)
        return True
    except ValueError:
        return False

@register.filter
def to_percentage(value):
    if is_number(value):
        return Decimal(value) * 100
    return value

@register.filter
def to_decimal(value):
    if is_number(value):
        return Decimal(value) / 100
    return value

@register.filter
def handle_percentage(value):
    if value is None or not hasattr(value, 'value'):
        return ""
    elif hasattr(value, 'field') and value.field.unit == "%":
        return to_percentage(value.value)
    else:
        return value.value
