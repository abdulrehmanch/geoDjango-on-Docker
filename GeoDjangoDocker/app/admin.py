from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import Location


# Register your models here.
@admin.register(Location)
class LocationAdmin(GISModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
