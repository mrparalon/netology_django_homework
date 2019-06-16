from django.shortcuts import render
from .models import Phone
from django.forms.models import model_to_dict


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    phones = Phone.objects.all()
    for phone in phones:
        if phone.brand == 'samsung':
            unique_params = phone.phonesamsung_set.all()
        elif phone.brand == 'apple':
            unique_params = phone.phoneapple_set.all().first()
            print(unique_params.phone.brand)
    return render(
        request,
        template,
        context
    )
