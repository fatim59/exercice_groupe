from django.urls import path
from conf import views

from . import views

urlpatterns = [
    path('about', views.about, name='about'), 
]