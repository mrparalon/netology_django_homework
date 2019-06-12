from django import template
import datetime


register = template.Library()


@register.filter
def format_date(value):
    now = datetime.datetime.utcnow()
    date = datetime.datetime.utcfromtimestamp(value)
    time_dif = now - date
    if time_dif < datetime.timedelta(seconds=600):
        value = 'только что'
    elif datetime.timedelta(hours=1) <= time_dif <= datetime.timedelta(hours=24):
        value = f"{str(int(time_dif.seconds/3600))} часов назад"
    else:
        value = date.strftime('%Y-%m-%d')
    return value


@register.filter
def format_score(value, default_value):
    if not value:
        result = default_value
    elif value < -5:
        result = 'все плохо'
    elif -5 <= value <= 5:
        result = 'нейтрально'
    elif value > 5:
        result = 'хорошо'
    return result


@register.filter
def format_num_comments(value):
    result = value
    if not value:
        result = 'Оставьте комментарий'
    elif value > 50:
        result = '50+'
    return result


@register.filter
def format_selftext(text, count):
    text = text.split()
    first_part = ' '.join(text[:count])
    last_part = ' '.join(text[-count:])
    result = f'{first_part} ... {last_part}'
    return result

