import ast

from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from django.template.defaultfilters import floatformat

register = template.Library()

@register.filter
def decorate_value(value, unit):
    try:
        value_dict = ast.literal_eval(value)
        if type(value_dict) is dict:
            if value_dict.get("type") == "Error" and value_dict.get("kind").lower() == "div":
                val = "DIV/0"
            elif value_dict.get("type") == "Error" and value_dict.get("kind").lower() == "na":
                val = "N/A"
            else:
                val = value_dict.get("kind")
            return val
        else:
            val = intcomma(floatformat(float(value), -2))
    except (ValueError, SyntaxError):
        val = value

    if val == "N/A":
        return val
    elif unit == "$":
        return f"${val}"
    elif unit:
        return f"{val} {unit}"
    
    return val
