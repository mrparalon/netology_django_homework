from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'review_count']
    list_filter = ['brand']
    search_fields = ['model']
    sortable_by = ['id']



class ReviewAdmin(admin.ModelAdmin):
    list_display = ['car', 'title']
    search_fields = ['car']
    list_filter = ['car__brand']
    form = ReviewAdminForm



admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
