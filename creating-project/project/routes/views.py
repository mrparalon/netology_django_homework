from django.shortcuts import render
from routes.models import Station, Route


def get_center(query):
    long_stations = query.order_by('longitude')
    lat_stations = query.order_by('latitude')
    first_by_long = long_stations.first()
    last_by_long = long_stations.last()
    first_by_lat = lat_stations.first()
    last_by_lat = lat_stations.last()
    print(first_by_lat.latitude, last_by_lat.latitude)
    if first_by_long != last_by_long:
        center_x = (last_by_long.longitude+first_by_long.longitude) / 2
    else:
        center_x = first_by_long.longitude
    if first_by_lat != last_by_lat:
        center_y = (last_by_lat.latitude+first_by_lat.latitude) / 2
    else:
        center_y = first_by_lat.latitude
    return center_x, center_y
    


def show_stations(request):
    stations = None
    center = {'x': 37.62, 'y': 55.750} #default center
    routes = Route.objects.all()
    if request.method == 'GET':
        route = request.GET.get('route')
        if route:
            stations = Station.objects.filter(routes__name=route)
            x, y = get_center(stations)
            center = {'x': x, 'y': y}
    template = 'stations.html'
    context = {'stations': stations,
               'routes': routes,
               'center': center}
    return render(request,
                  template,
                  context=context)
