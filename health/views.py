from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize

from .models import HealthCentre
# Create your views here.
def health_facilities(request):
    facilities = HealthCentre.objects.all()
    data = serialize('geojson', facilities)
    return HttpResponse(data)
