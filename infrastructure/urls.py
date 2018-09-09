from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/(?P<name>\w+)/$', views.endpoint),


    
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