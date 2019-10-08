
from django.urls import path
from resto import views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.menu, name='menu'),
    path('team', views.team, name='team'),
    path('dishes', views.dishes, name='dishes'),
   
]
