from django import template

register = template.Library()

@register.filter
def is_none(value):
    if value == '' or value == None: return '---- ----'
    return value
