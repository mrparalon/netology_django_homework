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


# необходимо добавить фильтр для поля `score`


@register.filter
def format_num_comments(value):
    # Ваш код
    return value



