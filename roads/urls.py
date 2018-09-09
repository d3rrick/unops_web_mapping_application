from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^assessed', views.assessed_roads)
]