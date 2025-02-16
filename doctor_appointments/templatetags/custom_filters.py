from django import template

register = template.Library()

@register.filter
def split(value, arg):
    """Splits a string by the given delimiter (arg)"""
    if value:
        return value.split(arg)
    return []