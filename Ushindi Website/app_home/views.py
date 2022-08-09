from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app_home/index.html')

def orphanhome(request):
    return render(request, 'app_home/orphanhome.html')

def highschool(request):
    return render(request, 'app_home/highschool.html')

def intermountain(request):
    return render(request, 'app_home/intermountain.html')

def ics(request):
    return render(request, 'app_home/ics.html')

def song(request):
    return render(request, 'app_home/song.html')

def projects(request):
    return render(request, 'app_home/projects.html')



