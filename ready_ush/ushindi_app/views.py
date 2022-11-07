from django.shortcuts import render, get_object_or_404
from django.views import generic 
from .models import *

# Create your views here.

def index(request):

    return render(request, 'ushindi_app/index.html')

def orphanhome(request):
    
    return render(request, 'ushindi_app/orphanhome.html')
    
def ics(request):

    return render(request, 'ushindi_app/intermountain.html')
    

def high(request):

    return render(request, 'ushindi_app/highschool.html')
    

def involved(request):

    return render(request, 'ushindi_app/involved.html')

def song(request):

    return render(request, 'ushindi_app/song.html')

def projects(request):

    return render(request, 'ushindi_app/projects.html')

