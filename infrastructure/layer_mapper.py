# ./manage.py ogrinspect data/roads/assessed/Assessed_Road.shp --srid=4326 --mapping --multi 


import os
from django.contrib.gis.utils import LayerMapping
from .models import BlockingPoint,CriticalPoint,ExtendedFoodDistribution,FoodDistribution,Market,Muddy,Bridge,RefugeeSettlement,Settlement,TradingCenter,TruckBlocking
# Auto-generated `LayerMapping` dictionary for BlockingPoint model
blockingpoint_mapping = {
    'image_numb' : 'Image_Numb',
    'road_surfa' : 'Road_surfa',
    'latitude' : 'Latitude',
    'longitute' : 'Longitute',
    'lengh' : 'Lengh',
    'type_of_po' : 'Type_of_po',
    'blocking_p' : 'blocking_p',
    'trucks_blo' : 'Trucks_Blo',
    'solution' : 'Solution',
    'geom' : 'MULTIPOINT',
}


criticalpoint_mapping = {
    'image_numb' : 'Image_Numb',
    'road_surfa' : 'Road_surfa',
    'latitude' : 'Latitude',
    'longitute' : 'Longitute',
    'lengh' : 'Lengh',
    'type_of_po' : 'Type_of_po',
    'blocking_p' : 'blocking_p',
    'trucks_blo' : 'Trucks_Blo',
    'solution' : 'Solution',
    'geom' : 'MULTIPOINT',
}

extendedfooddistribution_mapping = {
    'name' : 'Name',
    'x' : 'X',
    'y' : 'Y',
    'geom' : 'MULTIPOINT',
}

# Auto-generated `LayerMapping` dictionary for FoodDistribution model
fooddistribution_mapping = {
    'id' : 'ID',
    'fdp_name' : 'FDP_Name',
    'latitude' : 'Latitude',
    'longitude' : 'Longitude',
    'demographi' : 'Demographi',
    'population' : 'Population',
    'zone' : 'Zone',
    'field1' : 'Field1',
    'type' : 'Type',
    'geom' : 'MULTIPOINT',
}

# Auto-generated `LayerMapping` dictionary for Market model
market_mapping = {
    'osm_id' : 'osm_id',
    'addr_distr' : 'addr_distr',
    'addr_subco' : 'addr_subco',
    'addr_paris' : 'addr_paris',
    'addr_settl' : 'addr_settl',
    'addr_place' : 'addr_place',
    'addr_block' : 'addr_block',
    'start_date' : 'start_date',
    'amenity' : 'amenity',
    'name' : 'name',
    'opening_ho' : 'opening_ho',
    'geom' : 'MULTIPOINT',
}

# Auto-generated `LayerMapping` dictionary for Muddy model
muddy_mapping = {
    'id' : 'Id',
    'type' : 'Type',
    'geom' : 'MULTILINESTRING',
} 

# Auto-generated `LayerMapping` dictionary for Bridge model
bridge_mapping = {
    'name' : 'Name',
    'latitude' : 'Latitude',
    'longitude' : 'Longitude',
    'geom' : 'MULTIPOINT',
}


# Auto-generated `LayerMapping` dictionary for RefugeeSettlement model
refugeesettlement_mapping = {
    'osm_id' : 'osm_id',
    'osm_way_id' : 'osm_way_id',
    'refugee' : 'refugee',
    'admin_leve' : 'admin_leve',
    'boundary' : 'boundary',
    'name' : 'name',
    'type' : 'type',
    'operator' : 'operator',
    'operator_t' : 'operator_t',
    'population' : 'population',
    'capacity' : 'capacity',
    'start_date' : 'start_date',
    'landuse' : 'landuse',
    'place' : 'place',
    'name_en' : 'name_en',
    'official_n' : 'official_n',
    'loc_name' : 'loc_name',
    'access' : 'access',
    'near_fid' : 'NEAR_FID',
    'near_dist' : 'NEAR_DIST',
    'near_angle' : 'NEAR_ANGLE',
    'geom' : 'MULTIPOLYGON',
}


# Auto-generated `LayerMapping` dictionary for Settlement model
settlement_mapping = {
    'osm_id' : 'osm_id',
    'osm_way_id' : 'osm_way_id',
    'refugee' : 'refugee',
    'admin_leve' : 'admin_leve',
    'boundary' : 'boundary',
    'name' : 'name',
    'type' : 'type',
    'operator' : 'operator',
    'operator_t' : 'operator_t',
    'population' : 'population',
    'capacity' : 'capacity',
    'start_date' : 'start_date',
    'landuse' : 'landuse',
    'place' : 'place',
    'name_en' : 'name_en',
    'official_n' : 'official_n',
    'loc_name' : 'loc_name',
    'access' : 'access',
    'near_fid' : 'NEAR_FID',
    'near_dist' : 'NEAR_DIST',
    'near_angle' : 'NEAR_ANGLE',
    'geom' : 'MULTIPOLYGON',
}

tradingcenter_mapping = {
    'objectid' : 'OBJECTID',
    'id' : 'ID',
    'name' : 'NAME',
    'district' : 'DISTRICT',
    'fid_1' : 'FID_1',
    'y733_field' : 'Y733_',
    'y733_id' : 'Y733_ID',
    'easting' : 'EASTING',
    'northing' : 'NORTHING',
    'zone' : 'ZONE',
    'northadj' : 'NORTHADJ',
    'gps_update' : 'GPS_UPDATE',
    'population' : 'POPULATION',
    'household_field' : 'HOUSEHOLD_',
    'power_supp' : 'POWER_SUPP',
    'supply1' : 'SUPPLY1',
    'action' : 'ACTION',
    'if_not_tc' : 'IF_NOT_TC',
    'no' : 'NO',
    'date_field' : 'DATE_',
    'area' : 'AREA',
    'hh' : 'HH',
    'pop' : 'POP',
    'ps_grid' : 'PS_GRID',
    'ps_minirid' : 'PS_MINIRID',
    'kva' : 'KVA',
    'hrs_day' : 'HRS_DAY',
    'note' : 'NOTE',
    'n28' : 'N28',
    'latitude' : 'Latitude',
    'longitude' : 'Longitude',
    'geom' : 'MULTIPOINT',
}

truckblocking_mapping = {
    'image_numb' : 'Image_Numb',
    'road_surfa' : 'Road_surfa',
    'latitude' : 'Latitude',
    'longitute' : 'Longitute',
    'lengh' : 'Lengh',
    'type_of_po' : 'Type_of_po',
    'blocking_p' : 'blocking_p',
    'trucks_blo' : 'Trucks_Blo',
    'solution' : 'Solution',
    'geom' : 'MULTIPOINT',
}

shp_paths = [
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Blocking_Point.shp'),),
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Critical_Point.shp'),),
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Extended_Food_Distribution_Points.shp'),),
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Food_Distribution_Points.shp'),),
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Market.shp'),),
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Muddy_Section.shp'),),
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Nara_River_Bridge.shp'),),
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Blocking_Point.shp'),),
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Settlement_Zone.shp'),),
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Trading_Center.shp'),),
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Truck_Blocking_Point.shp'),)

]

model_data = [
    BlockingPoint,
    CriticalPoint,
    ExtendedFoodDistribution,
    FoodDistribution,
    Market,
    Muddy,
    Bridge,
    RefugeeSettlement,
    Settlement,
    TradingCenter,
    TruckBlocking,
]    
mappings = [
    blockingpoint_mapping, 
    criticalpoint_mapping, 
    extendedfooddistribution_mapping,
    fooddistribution_mapping,
    market_mapping,
    muddy_mapping,
    bridge_mapping,
    refugeesettlement_mapping,
    settlement_mapping,
    tradingcenter_mapping,
    truckblocking_mapping
]

def run(verbose=True):
    for i in range(12):
        lm = LayerMapping(model_data[i],shp_paths[i],mappings[i],
            transform=False, encoding='iso-8859-1',
        )
        lm.save(strict=True, verbose=verbose)
    

