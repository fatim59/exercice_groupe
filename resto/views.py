from django.shortcuts import render
from . models import *

def index(request):
    context = {
        'dishess':Dishes.objects.all(),
        'changes': Change.objects.all(),
    }
    return render(request, 'pages/index.html', context)


def menu(request):
    context = {
        'menus':Menu.objects.all(),
        'ingredients':Ingredient.objects.all(),
        'changes': Change.objects.all(),
        'dishess':Dishes.objects.all(),
    }
    return render(request, 'pages/menu.html', context)


def team(request):
    context = {
        'jobs':Job.objects.all(),
        'chefs':Chef.objects.all(),
        'dishess':Dishes.objects.all(),
        'changes': Change.objects.all(),
    }
    return render(request, 'pages/team.html', context)


def dishes(request):
    context = {
        'dishess':Dishes.objects.all(),
        'changes': Change.objects.all(),
    }
    return render(request, 'pages/dishes.html', context)



# Create your views here.
