from django.shortcuts import render
from . models import *

def index(request):
    return render(request, 'pages/index.html')


def menu(request):
    context = {
        'menus':Menu.objects.all(),
        'ingredients':Ingredient.objects.all(),
    }
    return render(request, 'pages/menu.html', context)


def team(request):
    context = {
        'jobs':Job.objects.all(),
        'chefs':Chef.objects.all(),
    }
    return render(request, 'pages/team.html', context)


def dishes(request):
    context = {
        'dishess':Dishes.objects.all(),
    }
    return render(request, 'pages/dishes.html', context)



# Create your views here.
