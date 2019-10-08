from django.urls import path
from client import views

from . import views

urlpatterns = [
    path('reservation', views.reservation, name='reservation'), 
]