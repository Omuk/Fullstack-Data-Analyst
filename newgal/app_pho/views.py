from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import *
# Create your views here.

def album(request):
    posts = Album.objects.all()
    return render(request, 'app_pho/gallery.html', {'posts':posts})

def album_view(request, id):
    album = get_object_or_404(Album, id=id)
    photos = AlbumPics.objects.filter(album=album)
    # context = {
    #     'post':post,
    #     'photos':photos
    # }

    return render(request, 'app_pho/album_pics.html', { 
        'post':album,
        'photos':photos
    })
