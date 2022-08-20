from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'app_ushindi/index.html')

def orphanhome(request):
    pass

def projects(request):
    pass
