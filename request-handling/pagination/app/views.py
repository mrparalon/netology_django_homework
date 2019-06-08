from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.conf import settings
from urllib.parse import urlencode
import os
from csv import DictReader
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    file_path = os.path.join(settings.BUS_STATION_CSV)
    current_page = request.GET.get('page')
    with open(file_path, encoding='cp1251') as csv_file:
        csv_data = list(DictReader(csv_file))
    if not current_page:
        current_page = 1
    current_page = int(current_page)
    paginator = Paginator(csv_data, 10)
    data = paginator.page(current_page)
    bus_stations_list = []
    for station in data:
        station_info_for_site = {'Name': station['Name'],
                                 'Street': station['Street'],
                                 'District': station['District']}
        bus_stations_list.append(station_info_for_site)
    url_begin = reverse(bus_stations)
    next_page_url = None
    prev_page_url = None
    if paginator.num_pages > current_page:
        next_page = current_page + 1
        next_page_url = f'{url_begin}?{urlencode({"page": next_page})}'
    if current_page >= 2:
        prev_page = current_page - 1
        prev_page_url = f'{url_begin}?{urlencode({"page": prev_page})}'
    return render_to_response('index.html', context={
        'bus_stations': bus_stations_list,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url
    })
