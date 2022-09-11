from django.urls import path
from .views import hub

urlpatterns = [
    path('', hub, name='hub'),
]