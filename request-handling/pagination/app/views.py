from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.conf import settings
from urllib.parse import urlencode
from csv import DictReader
from itertools import islice
import os


def index(request):
    return redirect(reverse(bus_stations))

def get_data_from_csv(data_file, page, list_size=10):
    with open(data_file, encoding='cp1251') as csv_file:
        csv_reader = DictReader(csv_file)
        start = (page - 1 ) * list_size
        stop = (page - 1) * list_size + list_size
        data = []
        for row in islice(csv_reader, start, stop):
            data.append(row)
        return data



def bus_stations(request):
    file_path = os.path.join(settings.BUS_STATION_CSV)
    current_page = request.GET.get('page')
    if not current_page:
        current_page = 1
    current_page = int(current_page)
    data = get_data_from_csv(file_path, current_page)
    bus_stations_list = []
    for station in data:
        station_info_for_site = {'Name': station['Name'],
                                 'Street': station['Street'],
                                 'District': station['District']}
        bus_stations_list.append(station_info_for_site)
    url_begin = reverse(bus_stations)
    next_page = current_page + 1
    print(url_begin)
    return render_to_response('index.html', context={
        'bus_stations': bus_stations_list,
        'current_page': current_page,
        'prev_page_url': None,
        'next_page_url': f'{url_begin}?{urlencode({"page": next_page})}'
    })

