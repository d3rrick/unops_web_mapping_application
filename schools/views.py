from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse


from .models import PrimarySchool,SecondarySchool,University

# Create your views here.

model_data = {
    "primary": PrimarySchool,
    "secondary": SecondarySchool,
    "university" : University
}

def school(request, name):
    model = model_data.get(name)
    passed = model.objects.all()
    data = serialize('geojson', passed)
    return HttpResponse(data)
