from django.contrib import admin
from .models import PrimarySchool,SecondarySchool,University
from django.contrib.gis import admin as geoAdmin
from leaflet.admin import LeafletGeoAdmin

class PrimarySchoolAdmin(geoAdmin.OSMGeoAdmin):
    # list_display = ('id', 'first_name', 'last_name', 'phone','date')
    # search_fields = ['first_name', 'phone']
    # ordering = ['id']
    # list_filter = ('id', 'phone')
    # default_lon = 4093226.24402 # 37.050093#
    # default_lat = -145706.24878 # -0.561360
    default_zoom = 14
    map_info = True
    map_width = 700
    map_height = 500
    # map_srid = 4326
class SecondarySchoolAdmin(geoAdmin.OSMGeoAdmin):
    # list_display = ('id', 'first_name', 'last_name', 'phone','date')
    # search_fields = ['first_name', 'phone']
    # ordering = ['id']
    # list_filter = ('id', 'phone')
    # default_lon = 4093226.24402 # 37.050093#
    # default_lat = -145706.24878 # -0.561360
    default_zoom = 14
    map_info = True
    map_width = 700
    map_height = 500
    # map_srid = 4326
class UniversityAdmin(geoAdmin.OSMGeoAdmin):
    # list_display = ('id', 'first_name', 'last_name', 'phone','date')
    # search_fields = ['first_name', 'phone']
    # ordering = ['id']
    # list_filter = ('id', 'phone')
    # default_lon = 4093226.24402 # 37.050093#
    # default_lat = -145706.24878 # -0.561360
    default_zoom = 14
    map_info = True
    map_width = 700
    map_height = 500
    # map_srid = 4326




admin.site.register(PrimarySchool, PrimarySchoolAdmin)
admin.site.register(SecondarySchool, SecondarySchoolAdmin)
admin.site.register(University, UniversityAdmin)