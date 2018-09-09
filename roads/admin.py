from django.contrib import admin
from .models import Road
from django.contrib.gis import admin as geoAdmin
from leaflet.admin import LeafletGeoAdmin

class AssessedRoadAdmin(geoAdmin.OSMGeoAdmin):
    # list_display = ('id', 'first_name', 'last_name', 'phone','date')
    # search_fields = ['first_name', 'phone']
    # ordering = ['id']
    # list_filter = ('id', 'phone')
    default_lon = 4093226.24402 # 37.050093#
    default_lat = -145706.24878 # -0.561360
    default_zoom = 14
    map_info = True
    map_width = 700
    map_height = 500
    srid = 32636



admin.site.register(Road, AssessedRoadAdmin)
