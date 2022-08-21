from django.shortcuts import render, get_object_or_404
from django.views import generic 
from .models import *

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

def song(request):

    # posts = BlogPost.objects.all()
    posts = Testimony.objects.all().order_by('-created_on')

    return render(request, 'app_ushindi/song.html', {'posts':posts})


class SongDetail(generic.DetailView):
    model = Testimony
    #full_song == post_detail
    template_name = 'app_ushindi/read_more.html'

def album(request):
    posts = Album.objects.all()
    return render(request, 'app_ushindi/gallery.html', {'posts':posts})

def album_view(request, id):
    album = get_object_or_404(Album, id=id)
    photos = AlbumPics.objects.filter(album=album)
    # context = {
    #     'post':post,
    #     'photos':photos
    # }

    return render(request, 'app_ushindi/album_pics.html', { 
        'post':album,
        'photos':photos
    })
