from django import template

register = template.Library()


@register.filter
def hyphen(value):
    print(type(value))
    if isinstance(value, bool):
        if value:
            value = 'Да'
        else:
            value = 'Нет'
    elif value == '':
        value = '-'
    return value
