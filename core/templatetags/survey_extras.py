from django import template

register = template.Library()

@register.filter(name='split')
def split(value, arg):
    return value.split(arg)

@register.filter(name='split_items')
def split_items(value):
    """
    Splits string like 'key:label,key2:label2' into list of (key, label)
    """
    items = []
    for pair in value.split(','):
        if ':' in pair:
            k, v = pair.split(':', 1)
            items.append((k.strip(), v.strip()))
    return items
