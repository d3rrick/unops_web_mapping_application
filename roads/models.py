from django.db import models
from django.contrib.gis.db import models as geomodels

class Road(models.Model):
    fid = models.FloatField()
    road_type = models.CharField(max_length=20)
    section = models.CharField(max_length=25)
    section_na = models.CharField(max_length=25)
    geom = geomodels.MultiLineStringField(srid=32636)
    


