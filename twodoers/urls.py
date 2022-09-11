from django.contrib import admin
from django.urls import path, include
from reports.views import dex

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('', dex, name='index'),
    path('reports/', include('reports.urls')),
    path('hub/', include('hub.urls')),
]
