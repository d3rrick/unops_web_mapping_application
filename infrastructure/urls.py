from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/(?P<name>\w+)/$', views.endpoint),
    url(r'^api/districts/$', views.districts),


    
]

# model_data = [
#     BlockingPoint,
#     CriticalPoint,
#     ExtendedFoodDistribution,
#     FoodDistribution,
#     Market,
#     Muddy,
#     Bridge,
#     RefugeeSettlement,
#     Settlement,
#     TradingCenter,
#     TruckBlocking,
# ]