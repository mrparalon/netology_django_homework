from django.core.management.base import BaseCommand
import csv
from routes.models import Route, Station

class Command(BaseCommand):
    help = 'Import station information from csv'

    def handle(self, *args, **options):
        with open('moscow_bus_stations.csv', encoding='cp1251') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')
            for station in reader:
                lat = float(station['Latitude_WGS84'])
                long = float(station['Longitude_WGS84']        long_stations = stations.order_by('longitude')
                routes = station['RouteNumbers'].split('; ')
                name = station['Name']
                routes_list = []
                for route in routes:
                    route_obj, created = Route.objects.get_or_create(name=route)
                    routes_list.append(route_obj)
                station_model, created = Station.objects.get_or_create(latitude=lat,
                                        longitude=long,
                                        name=name)
                print(station_model.id, station_model)
                station_model.routes.add(*routes_list)
        return 'Stations imported'
