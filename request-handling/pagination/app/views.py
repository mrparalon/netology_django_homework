from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.conf import settings
from csv import DictReader
from itertools import islice
import os


def index(request):
    return redirect(reverse(bus_stations))

def get_data_from_csv(data_file, page):
    with open(data_file, encoding='cp1251') as csv_file:
        csv_reader = DictReader(csv_file)
        # data = csv_reader[(page - 1 ) * 10, (page - 1) * 10 - 10]
        start = (page - 1 ) * 10
        stop = (page - 1) * 10 + 10
        data = []
        for row in islice(csv_reader, start, stop):
            data.append(row)
        return data



def bus_stations(request):
    file_path = os.path.join(settings.BUS_STATION_CSV)
    data = get_data_from_csv(file_path, 2)
    bus_stations = []
    for station in data:
        station_info_for_site = {'Name': station['Name'],
                                 'Street': station['Street'],
                                 'District': station['District']}
        bus_stations.append(station_info_for_site)
    return render_to_response('index.html', context={
        'bus_stations': bus_stations,
        'current_page': 1,
        'prev_page_url': None,
        'next_page_url': 'bus_stations/?page=2',
    })

