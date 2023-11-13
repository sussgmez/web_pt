from django import template

register = template.Library()

@register.filter
def not_closed(value):
    return value.filter(closed=False)

@register.filter
def only_100_chars(value):
    try: 
        return value[:100]
    except: 
        pass
    return value
