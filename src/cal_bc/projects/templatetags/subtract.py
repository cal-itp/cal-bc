from django import template

register = template.Library()

@register.filter
def subtract(value: any, arg: any) -> any:
    try:
        return int(value) - int(arg)
    except (ValueError, TypeError):
        return ""
