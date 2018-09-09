from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse,JsonResponse

from .models import Districts,HealthCentre, BlockingPoint,CriticalPoint,ExtendedFoodDistribution,FoodDistribution,Market,Muddy,Bridge,RefugeeSettlement,Settlement,TradingCenter,TruckBlocking



model_data = {
    "districts" : Districts,
    'health' : HealthCentre,
    'blocking' : BlockingPoint,
    'critical' : CriticalPoint,
    'extended' : ExtendedFoodDistribution,
    'food': FoodDistribution,
    'market': Market,
    'muddy' : Muddy,
    'bridge': Bridge,
    'refugee' : RefugeeSettlement,
    'settlement' : Settlement,
    'trading' : TradingCenter,
    'truck' : TruckBlocking
}

def endpoint(request,name):
    if name is not "health":
        model = model_data.get(name)
        passed = model.objects.all()
        data = serialize('geojson', passed)
        return HttpResponse(data)
    else:
        filter_facilities()


def filter_facilities():
    districts = Districts.objects.all()
    print("original", len(districts))
    facilities = HealthCentre.objects.all()
    data = []

    for f in facilities:
        for d in districts:
            if d.wkb_geometry.contains(f.geom):
                data.append(f)
    print(len(data))

    return HttpResponse(serialize('geojson', data),data=len(data))



# def county_data(request):
#     points = Accident.objects.all()
#     counties = County.objects.all()
#     data = []

#     for a in points:
#         for c in counties:
#             if c.geom.contains(a.location):
#                 data.append(c)

#     return JsonResponse(data,safe=False)
    


