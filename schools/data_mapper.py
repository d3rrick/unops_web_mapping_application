
import os
from django.contrib.gis.utils import LayerMapping
from .models import PrimarySchool,SecondarySchool,University



# Auto-generated `LayerMapping` dictionary for all models


primaryschool_mapping = {
    'osm_id' : 'osm_id',
    'addr_distr' : 'addr_distr',
    'addr_count' : 'addr_count',
    'addr_subco' : 'addr_subco',
    'addr_paris' : 'addr_paris',
    'addr_villa' : 'addr_villa',
    'addr_settl' : 'addr_settl',
    'addr_zone' : 'addr_zone',
    'addr_point' : 'addr_point',
    'addr_block' : 'addr_block',
    'name' : 'name',
    'start_date' : 'start_date',
    'amenity' : 'amenity',
    'isced_leve' : 'isced_leve',
    'opening_ho' : 'opening_ho',
    'phone' : 'phone',
    'operator' : 'operator',
    'operator_t' : 'operator_t',
    'social_fac' : 'social_fac',
    'social_f_1' : 'social_f_1',
    'temporary' : 'temporary',
    'toilets' : 'toilets',
    'capacity' : 'capacity',
    'staff_coun' : 'staff_coun',
    'generator_field' : 'generator_',
    'water_supp' : 'water_supp',
    'drinking_w' : 'drinking_w',
    'fee' : 'fee',
    'school_typ' : 'School_Typ',
    'latitude' : 'Latitude',
    'longitude' : 'Longitude',
    'geom' : 'MULTIPOINT',
}

secondaryschool_mapping = {
    'no_field' : 'No_',
    'district' : 'District',
    'settlement' : 'Settlement',
    'location' : 'Location',
    'name' : 'Name',
    'lat_n' : 'Lat_N',
    'long_e' : 'Long_E',
    'osm_id' : 'osm_id',
    'addr_distr' : 'addr_distr',
    'addr_count' : 'addr_count',
    'addr_subco' : 'addr_subco',
    'addr_paris' : 'addr_paris',
    'addr_villa' : 'addr_villa',
    'addr_settl' : 'addr_settl',
    'addr_zone' : 'addr_zone',
    'addr_point' : 'addr_point',
    'addr_block' : 'addr_block',
    'start_date' : 'start_date',
    'amenity' : 'amenity',
    'isced_leve' : 'isced_leve',
    'opening_ho' : 'opening_ho',
    'phone' : 'phone',
    'operator' : 'operator',
    'operator_t' : 'operator_t',
    'social_fac' : 'social_fac',
    'social_f_1' : 'social_f_1',
    'temporary' : 'temporary',
    'toilets' : 'toilets',
    'capacity' : 'capacity',
    'staff_coun' : 'staff_coun',
    'generator_field' : 'generator_',
    'water_supp' : 'water_supp',
    'drinking_w' : 'drinking_w',
    'fee' : 'fee',
    'school_typ' : 'School_Typ',
    'geom' : 'MULTIPOINT',
}

university_mapping = {
    'osm_id' : 'osm_id',
    'addr_distr' : 'addr_distr',
    'addr_count' : 'addr_count',
    'addr_subco' : 'addr_subco',
    'addr_paris' : 'addr_paris',
    'addr_villa' : 'addr_villa',
    'addr_settl' : 'addr_settl',
    'addr_zone' : 'addr_zone',
    'addr_point' : 'addr_point',
    'addr_block' : 'addr_block',
    'name' : 'name',
    'start_date' : 'start_date',
    'amenity' : 'amenity',
    'isced_leve' : 'isced_leve',
    'opening_ho' : 'opening_ho',
    'phone' : 'phone',
    'operator' : 'operator',
    'operator_t' : 'operator_t',
    'social_fac' : 'social_fac',
    'social_f_1' : 'social_f_1',
    'temporary' : 'temporary',
    'toilets' : 'toilets',
    'capacity' : 'capacity',
    'staff_coun' : 'staff_coun',
    'generator_field' : 'generator_',
    'water_supp' : 'water_supp',
    'drinking_w' : 'drinking_w',
    'fee' : 'fee',
    'school_typ' : 'School_Typ',
    'geom' : 'MULTIPOINT',
}

primary_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Primary_School.shp'),)
secondary_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Secondary_School.shp'),)
university_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'University.shp'),)



def primary(verbose=True):
    lm = LayerMapping(
        PrimarySchool, primary_shp, primaryschool_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)

def secondary(verbose=True):
    lm = LayerMapping(
        SecondarySchool, secondary_shp, secondaryschool_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)

def university(verbose=True):
    lm = LayerMapping(
        University, university_shp, university_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)

def run():
    primary()
    secondary()
    university()

