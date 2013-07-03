from django.contrib import admin
from models import Event, Location


class LocationAdmin(admin.ModelAdmin):
    list_display = ('address', 'city', 'province')
admin.site.register(Location, LocationAdmin)


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time')
admin.site.register(Event, EventAdmin)
