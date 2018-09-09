import os
from django.contrib.gis.utils import LayerMapping
from .models import HealthCentre


# Auto-generated `LayerMapping` dictionary for HealthCentre model
healthcentre_mapping = {
    'objectid' : 'OBJECTID',
    'name' : 'Name',
    'lat' : 'Lat',
    'lon' : 'Lon',
    'osm_id' : 'osm_id',
    'timestamp' : 'timestamp',
    'district' : 'District',
    'county' : 'County',
    'subcounty' : 'Subcounty',
    'source' : 'Source',
    'collection' : 'Collection',
    'collecti_1' : 'Collecti_1',
    'grade' : 'Grade',
    'ownership' : 'Ownership',
    'grid_dista' : 'Grid_Dista',
    'hc_name' : 'HC_NAME',
    'hc_type' : 'HC_TYPE',
    'status' : 'STATUS',
    'x_raw' : 'X_RAW',
    'y_raw' : 'Y_RAW',
    'dname_2006' : 'DNAME_2006',
    'cname_2006' : 'CNAME_2006',
    'sname_2006' : 'SNAME_2006',
    'pname_2006' : 'PNAME_2006',
    'dname_2010' : 'DNAME_2010',
    'sname_2010' : 'SNAME_2010',
    'subregion' : 'SUBREGION',
    'country' : 'COUNTRY',
    'x_utm' : 'X_UTM',
    'y_utm200k' : 'Y_UTM200K',
    'geom' : 'MULTIPOINT',
}


health_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Health_Facilities.shp'),)

def run(verbose=True):
    lm = LayerMapping(
        HealthCentre, health_shp, healthcentre_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)