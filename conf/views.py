from django.shortcuts import render
from . models import *

def about(request):   
    context ={
        'abouts':About.objects.all(),
        'recipes':Recipe.objects.all(),
        'changes': Change.objects.all(),
        'dishess':Dishes.objects.all(),
    } 
    return render(request, 'pages/about.html', context)
