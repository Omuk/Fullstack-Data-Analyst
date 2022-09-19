from django.shortcuts import render, get_object_or_404
from django.views import generic 
from .models import *

# Create your views here.

def index(request):

    return render(request, 'app_ushindi/index.html')

def orphanhome(request):
    
    return render(request, 'app_ushindi/orphanhome.html')
    


def ics(request):

    return render(request, 'app_ushindi/inter.html')


def high(request):

    return render(request, 'app_ushindi/high.html')

def involved(request):

    return render(request, 'app_ushindi/involved.html')

def albums(request):

    return render(request, 'app_ushindi/albums.html')


def song(request):

    # posts = BlogPost.objects.all()
    posts = Testimony.objects.all().order_by('-created_on')

    return render(request, 'app_ushindi/song.html', {'posts':posts})


class SongDetail(generic.DetailView):
    model = Testimony
    #full_song == post_detail
    template_name = 'app_ushindi/read_more.html'

def gallery_album(request):
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


def projects(request):

    posts = ProjEvents.objects.all()
    

    return render(request, 'app_ushindi/projects.html', {'posts': posts})

def proj_detail(request, id):
    album = get_object_or_404(ProjEvents, id=id)
    photos = ProjDetails.objects.filter(album=album)
    # context = {
    #     'post':post,
    #     'photos':photos
    # }

    return render(request, 'app_ushindi/proj_detail.html', { 
        'post':album,
        'photos':photos
    })


class ProjectDetail(generic.DetailView):
    model = ProjEvents
    #full_song == post_detail
    template_name = 'app_ushindi/proj_detail.html'
