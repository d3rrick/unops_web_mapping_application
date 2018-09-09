# ./manage.py ogrinspect data/roads/assessed/Assessed_Road.shp --srid=4326 --mapping --multi 


import os
from django.contrib.gis.utils import LayerMapping
from .models import Road
# Auto-generated `LayerMapping` dictionary for AssessedRoad model
road_mapping = {
    'fid' : 'fid',
    'road_type' : 'Road_Type',
    'section' : 'Section',
    'section_na' : 'Section_Na',
    'geom' : 'MULTILINESTRING',
}


assessedroad_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/assessed', 'accessed.shp'),)

def run(verbose=True):
    lm = LayerMapping(
        Road, assessedroad_shp, road_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)

