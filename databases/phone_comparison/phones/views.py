from django.shortcuts import render
from .models import Phone
from django.forms.models import model_to_dict


def get_phone_data_list(brand_phone_query):
    result = []
    for brand_phone in brand_phone_query:
        phone_data = model_to_dict(brand_phone.phone)
        phone_data.pop('id', None)
        add_data = model_to_dict(brand_phone)
        add_data.pop('id', None)
        add_data.pop('phone', None)
        phone_data.update(add_data)
        result.append(phone_data)
        return result


def show_catalog(request):
    template = 'catalog.html'
    context = {'phones': []}
    phones = Phone.objects.all()
    for phone in phones:
        if phone.brand == 'samsung':
            unique_params = phone.phonesamsung_set.all()
            context['phones'] += unique_params
            # phone_data = get_phone_data_list(unique_params)
            # for all_data_phone in phone_data:
            #     context['phones'].append(all_data_phone)
        elif phone.brand == 'apple':
            unique_params = phone.phoneapple_set.all()
            context['phones'] += unique_params
            # phone_data = get_phone_data_list(unique_params)
            # for all_data_phone in phone_data:
            #     context['phones'].append(all_data_phone)
    return render(
        request,
        template,
        context
    )
