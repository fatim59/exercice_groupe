from django.shortcuts import render
from . models import *

def reservation(request):
    return render(request, 'pages/reservation.html')

# Create your views here.
