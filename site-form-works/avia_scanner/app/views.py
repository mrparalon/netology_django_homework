import time
import random

from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


def ticket_page_view(request):
    template = 'app/ticket_page.html'

    context = {
        'form': SearchTicket()
    }

    return render(request, template, context)


def cities_lookup(request):
    city_name = request.GET['term'].lower()
    if not cache.get('cities'):
        cities = City.objects.all()
        cities_list = [city.name.lower() for city in cities]
        cache.set('cities', cities_list)
    else:
        cities_list = cache.get('cities')
    results = [city.capitalize() for city in cities_list if city_name in city]
    return JsonResponse(results, safe=False)
