from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^facilities', views.health_facilities)
]