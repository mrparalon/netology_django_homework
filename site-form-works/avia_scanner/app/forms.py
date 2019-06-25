from django import forms

from .widgets import AjaxInputWidget
from .models import City


class SearchTicket(forms.Form):
    departure_city = forms.CharField(widget=AjaxInputWidget('/api/city_ajax',
                                                            attrs={'class': 'inline right_matgin'}))
    arival_city = forms.CharField(widget=AjaxInputWidget('/api/city_ajax',
                                                         attrs={'class': 'inline right_matgin'}))
    date = forms.DateField(widget=forms.SelectDateWidget)
