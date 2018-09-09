from django.db import models
from django.contrib.gis.db import models as geomodels

# DELETE FROM django_migrations WHERE app='your-app-name'
# Create your models here.
class BlockingPoint(models.Model):
    image_numb = models.IntegerField()
    road_surfa = models.CharField(max_length=254)
    latitude = models.FloatField()
    longitute = models.FloatField()
    lengh = models.IntegerField()
    type_of_po = models.CharField(max_length=254)
    blocking_p = models.CharField(max_length=254)
    trucks_blo = models.CharField(max_length=254)
    solution = models.CharField(max_length=254)
    geom = geomodels.MultiPointField(srid=4326)


class CriticalPoint(models.Model):
    image_numb = models.IntegerField()
    road_surfa = models.CharField(max_length=254)
    latitude = models.FloatField()
    longitute = models.FloatField()
    lengh = models.IntegerField()
    type_of_po = models.CharField(max_length=254)
    blocking_p = models.CharField(max_length=254)
    trucks_blo = models.CharField(max_length=254)
    solution = models.CharField(max_length=254)
    geom = geomodels.MultiPointField(srid=4326)





class ExtendedFoodDistribution(models.Model):
    name = models.CharField(max_length=254)
    x = models.FloatField()
    y = models.FloatField()
    geom = geomodels.MultiPointField(srid=4326)




class FoodDistribution(models.Model):
    id = models.IntegerField(primary_key=True)
    fdp_name = models.CharField(max_length=254)
    latitude = models.FloatField()
    longitude = models.FloatField()
    demographi = models.IntegerField()
    population = models.IntegerField()
    zone = models.CharField(max_length=254)
    field1 = models.CharField(max_length=254)
    type = models.CharField(max_length=254)
    geom = geomodels.MultiPointField(srid=4326)





class Market(models.Model):
    osm_id = models.CharField(max_length=80)
    addr_distr = models.CharField(max_length=80)
    addr_subco = models.CharField(max_length=80)
    addr_paris = models.CharField(max_length=80)
    addr_settl = models.CharField(max_length=80)
    addr_place = models.CharField(max_length=80)
    addr_block = models.CharField(max_length=80)
    start_date = models.CharField(max_length=80)
    amenity = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    opening_ho = models.CharField(max_length=80)
    geom = geomodels.MultiPointField(srid=4326)



class Muddy(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=15)
    geom = geomodels.MultiLineStringField(srid=4326)


class Bridge(models.Model):
    name = models.CharField(max_length=254)
    latitude = models.FloatField()
    longitude = models.FloatField()
    geom = geomodels.MultiPointField(srid=4326)


class RefugeeSettlement(models.Model):
    osm_id = models.CharField(max_length=80)
    osm_way_id = models.CharField(max_length=80)
    refugee = models.CharField(max_length=80)
    admin_leve = models.CharField(max_length=80)
    boundary = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    type = models.CharField(max_length=80)
    operator = models.CharField(max_length=80)
    operator_t = models.CharField(max_length=80)
    population = models.CharField(max_length=80)
    capacity = models.CharField(max_length=80)
    start_date = models.CharField(max_length=80)
    landuse = models.CharField(max_length=80)
    place = models.CharField(max_length=80)
    name_en = models.CharField(max_length=80)
    official_n = models.CharField(max_length=80)
    loc_name = models.CharField(max_length=80)
    access = models.CharField(max_length=80)
    near_fid = models.IntegerField()
    near_dist = models.FloatField()
    near_angle = models.FloatField()
    geom = geomodels.MultiPolygonField(srid=4326)


class Settlement(models.Model):
    osm_id = models.CharField(max_length=80)
    osm_way_id = models.CharField(max_length=80)
    refugee = models.CharField(max_length=80)
    admin_leve = models.CharField(max_length=80)
    boundary = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    type = models.CharField(max_length=80)
    operator = models.CharField(max_length=80)
    operator_t = models.CharField(max_length=80)
    population = models.CharField(max_length=80)
    capacity = models.CharField(max_length=80)
    start_date = models.CharField(max_length=80)
    landuse = models.CharField(max_length=80)
    place = models.CharField(max_length=80)
    name_en = models.CharField(max_length=80)
    official_n = models.CharField(max_length=80)
    loc_name = models.CharField(max_length=80)
    access = models.CharField(max_length=80)
    near_fid = models.IntegerField()
    near_dist = models.FloatField()
    near_angle = models.FloatField()
    geom = geomodels.MultiPolygonField(srid=4326)



class TradingCenter(models.Model):
    objectid = models.IntegerField()
    id = models.CharField(primary_key=True,max_length=14)
    name = models.CharField(max_length=20)
    district = models.CharField(max_length=14)
    fid_1 = models.CharField(max_length=8)
    y733_field = models.CharField(max_length=8)
    y733_id = models.CharField(max_length=8)
    easting = models.FloatField()
    northing = models.FloatField()
    zone = models.CharField(max_length=10)
    northadj = models.FloatField()
    gps_update = models.CharField(max_length=11)
    population = models.CharField(max_length=6)
    household_field = models.CharField(max_length=11)
    power_supp = models.CharField(max_length=9)
    supply1 = models.CharField(max_length=9)
    action = models.CharField(max_length=10)
    if_not_tc = models.CharField(max_length=12)
    no = models.CharField(max_length=9)
    date_field = models.DateField(null=True, blank=True)
    area = models.CharField(max_length=9)
    hh = models.IntegerField()
    pop = models.IntegerField()
    ps_grid = models.CharField(max_length=9)
    ps_minirid = models.CharField(max_length=9)
    kva = models.CharField(max_length=9)
    hrs_day = models.CharField(max_length=9)
    note = models.CharField(max_length=9)
    n28 = models.CharField(max_length=9)
    latitude = models.FloatField()
    longitude = models.FloatField()
    geom = geomodels.MultiPointField(srid=4326)


class TruckBlocking(models.Model):
    image_numb = models.IntegerField()
    road_surfa = models.CharField(max_length=254)
    latitude = models.FloatField()
    longitute = models.FloatField()
    lengh = models.IntegerField()
    type_of_po = models.CharField(max_length=254)
    blocking_p = models.CharField(max_length=254)
    trucks_blo = models.CharField(max_length=254)
    solution = models.CharField(max_length=254)
    geom = geomodels.MultiPointField(srid=4326)

class HealthCentre(models.Model):
    objectid = models.IntegerField()
    name = models.CharField(max_length=254)
    lat = models.FloatField()
    lon = models.FloatField()
    osm_id = models.FloatField()
    timestamp = models.CharField(max_length=20)
    district = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    subcounty = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    collection = models.CharField(max_length=50)
    collecti_1 = models.CharField(max_length=50)
    grade = models.CharField(max_length=50)
    ownership = models.CharField(max_length=50)
    grid_dista = models.CharField(max_length=50)
    hc_name = models.CharField(max_length=254)
    hc_type = models.CharField(max_length=254)
    status = models.CharField(max_length=254)
    x_raw = models.FloatField()
    y_raw = models.FloatField()
    dname_2006 = models.CharField(max_length=254)
    cname_2006 = models.CharField(max_length=254)
    sname_2006 = models.CharField(max_length=254)
    pname_2006 = models.CharField(max_length=254)
    dname_2010 = models.CharField(max_length=254)
    sname_2010 = models.CharField(max_length=254)
    subregion = models.CharField(max_length=254)
    country = models.CharField(max_length=254)
    x_utm = models.FloatField()
    y_utm200k = models.FloatField()
    geom = geomodels.MultiPointField(srid=32636)


class Districts(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    objectid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    dname2014 = models.CharField(max_length=80, blank=True, null=True)
    subregion = models.CharField(max_length=80, blank=True, null=True)
    region = models.CharField(max_length=80, blank=True, null=True)
    hh2014 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    hhsize2014 = models.DecimalField(max_digits=19, decimal_places=11, blank=True, null=True)
    males2014 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    female2014 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    pop_2014 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    pop_urban = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    pop_rural = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    pop2013 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    pop2010 = models.DecimalField(max_digits=19, decimal_places=11, blank=True, null=True)
    hh2010 = models.DecimalField(max_digits=19, decimal_places=11, blank=True, null=True)
    pop2002 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    hh2002 = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    f1991_2002 = models.DecimalField(max_digits=19, decimal_places=11, blank=True, null=True)
    f2002_2014 = models.DecimalField(max_digits=19, decimal_places=11, blank=True, null=True)
    f1969_2014 = models.DecimalField(max_digits=19, decimal_places=11, blank=True, null=True)
    totcon2011 = models.DecimalField(max_digits=19, decimal_places=11, blank=True, null=True)
    accs_ele_h = models.DecimalField(max_digits=19, decimal_places=11, blank=True, null=True)
    status = models.CharField(max_length=80, blank=True, null=True)
    globalid = models.CharField(max_length=80, blank=True, null=True)
    creationda = models.DateField(blank=True, null=True)
    creator = models.CharField(max_length=80, blank=True, null=True)
    editdate = models.DateField(blank=True, null=True)
    editor = models.CharField(max_length=80, blank=True, null=True)
    rai = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    rai_urb = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    rai_ub_pop = models.DecimalField(max_digits=13, decimal_places=11, blank=True, null=True)
    new_rai = models.DecimalField(max_digits=13, decimal_places=11, blank=True, null=True)
    wkb_geometry = geomodels.PolygonField(srid=4326,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'districts'
        verbose_name_plural = "District"
    
    def __str__(self):
        return self.dname2014
