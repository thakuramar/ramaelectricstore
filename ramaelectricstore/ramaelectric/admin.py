from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Items, AppointmentForm


class ItemsAdmin(ImportExportModelAdmin):
    pass


# Register your models here.
admin.site.register(Items, ItemsAdmin)

admin.site.register(AppointmentForm)

