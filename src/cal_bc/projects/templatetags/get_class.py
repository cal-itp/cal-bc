from django import template

register = template.Library()


@register.filter
def get_class(value):
    return value.__class__.__name__


@register.filter
def get_dir(value):
    return dir(value)
