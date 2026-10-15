from django import template

register = template.Library()

@register.filter
def max_attr(set: list[any], attr: str) -> any:
    return max([getattr(s, attr) for s in set]) if len(set) else 0
