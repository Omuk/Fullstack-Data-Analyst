from django.shortcuts import render

# Create your views here.

# def index(request):
#     return render(request, 'app_home/index.html')

def index(request):
    return render(request, 'app_home/home.html')

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

def alumni(request):
    return render(request, 'app_home/alumni.html')

def widows(request):
    return render(request, 'app_home/widows.html')

def poormin(request):
    return render(request, 'app_home/poormin.html')



