from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse

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
    model = model_data.get(name)
    passed = model.objects.all()
    data = serialize('geojson', passed)
    return HttpResponse(data)

def districts(request):
    model = Districts.objects.all()
    passed = model.objects.all()
    data = serialize('geojson', passed)
    return HttpResponse(data)


