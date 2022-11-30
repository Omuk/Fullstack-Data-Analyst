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


def gallery_album(request):
    
    return render(request, 'ushindi_app/gallery_cover.html')

def mem_view(request):

    return render(request, 'ushindi_app/gal_mem_pics.html')


def agr_view(request):

    return render(request, 'ushindi_app/gal_agr_pics.html')

def alum_view(request):

    return render(request, 'ushindi_app/gal_alum_pics.html')


def beg_view(request):

    return render(request, 'ushindi_app/gal_beg_pics.html') 


def cul_view(request):

    return render(request, 'ushindi_app/gal_cul_pics.html') 


def exc_view(request):

    return render(request, 'ushindi_app/gal_exc_pics.html') 

def high_view(request):

    return render(request, 'ushindi_app/gal_high_pics.html') 

def inter_view(request):

    return render(request, 'ushindi_app/gal_inter_pics.html')

def kid_view(request):

    return render(request, 'ushindi_app/gal_kid_pics.html') 

def mom_view(request):

    return render(request, 'ushindi_app/gal_mom_pics.html') 

def sol_view(request):

    return render(request, 'ushindi_app/gal_sol_pics.html')
