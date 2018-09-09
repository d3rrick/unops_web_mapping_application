
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('portal.urls')),
    url(r'^roads/', include('roads.urls')),
    url(r'^schools/', include('schools.urls')),
    url(r'^health/', include('health.urls')),
    url(r'^infrastructure/', include('infrastructure.urls')),
    url(r'^admin/', admin.site.urls),
]
