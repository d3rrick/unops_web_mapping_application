from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from django.contrib.gis.geos import GEOSGeometry

from .models import Road
def assessed_roads(request):
    assessed = Road.objects.all()
    data = serialize('geojson', assessed)
    return HttpResponse(data)
    

# def assessed_roads(request):
#     # roads = AssessedRoad.objects.raw("SELECT road_type,section,section_na,ST_AsText(wkb_geometry) FROM towns")
#     # ST_AsText(ST_Transform(ST_GeomFromText(geom,32636),4326))
#     roads = AssessedRoad.objects.raw("SELECT id,road_type,section,geom FROM roads_assessedroad")
#     point = AssessedRoad.objects.get(id=1)
#     pnt = GEOSGeometry('010100000000000000000014400000000000003740')
#     print(point.geom)
#     data = serialize('geojson', roads)
#     return HttpResponse(data)


