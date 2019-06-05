from django import template

register = template.Library()


@register.filter
def inflation_color(inflation, column, name='inflation_color'):
    # Мне кажется, if-ов многовато, но лучше я не придумал
    color = None
    if inflation:
        inflation = float(inflation)
        if inflation < 0:
            color = '#00e86d'
        elif 1 < inflation <= 2:
            color = '#ffa0a0'
        elif 2 < inflation <= 5:
            color = '#ff3d3d'
        elif inflation > 5:
            color = '#9f0000'
    else:
        inflation = '-'
    if column == 'Суммарная':
        color = '#c9c9c9'
    if color:
        table_data_cell = f'<td bgcolor={color}>{inflation}</td>'
    else:
        table_data_cell = f'<td>{inflation}</td>'
    return table_data_cell
