from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/(?P<name>\w+)/$', views.school),
    
]