from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'app_ushindi/index.html')

def orphanhome(request):
    
    return render(request, 'app_ushindi/orphanhome.html')
    

def projects(request):
    pass

def ics(request):

    return render(request, 'app_ushindi/inter.html')


def high(request):

    return render(request, 'app_ushindi/high.html')
