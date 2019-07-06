from django.contrib import admin
from .models import Table, Path

class TableAdimn(admin.ModelAdmin):
    pass


class PathAdmin(admin.ModelAdmin):
    pass


admin.site.register(Table, TableAdimn)
admin.site.register(Path, PathAdmin)
