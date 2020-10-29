from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Items, AppointmentForm


class ItemsAdmin(ImportExportModelAdmin):
    list_display = ['name', 'updated_on']
    search_fields = ['name', 'brand', 'arrival_date']
    list_filter = ['updated_on']


# Register your models here.
admin.site.register(Items, ItemsAdmin)

admin.site.register(AppointmentForm)

