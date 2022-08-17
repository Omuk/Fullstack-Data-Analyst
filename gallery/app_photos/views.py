from django.shortcuts import render
from .models import *

# Create your views here.

def gallery(request):
    posts = GalleryPoster.objects.all()

    return render(request, 'app_photos/gallery.html', {'posts':posts})
