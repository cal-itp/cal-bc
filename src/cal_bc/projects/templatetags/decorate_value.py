from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from django.template.defaultfilters import floatformat

register = template.Library()

@register.filter
def decorate_value(value, unit):
     try:
         val = intcomma(floatformat(float(value), -2))
     except ValueError:
         val = value

     if value == "N/A":
         return val
     elif unit == "$":
         return f"${val}"
     elif unit:
         return f"{val} {unit}"

     return val
