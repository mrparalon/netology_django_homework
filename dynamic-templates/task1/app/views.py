from django.shortcuts import render
from csv import DictReader
import os

def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    file_path = os.path.join(os.path.dirname(__file__), '..', 'inflation_russia.csv')
    with open(file_path) as csv_file:
        csv_data = list(DictReader(csv_file, delimiter=';'))
    headers = csv_data[0].keys()
    context = {'table': csv_data, 'csv_headers': headers}
    return render(request, template_name,
                  context)