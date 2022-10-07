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

    posts = Testimony.objects.all().order_by('-created_on')

    return render(request, 'ushindi_app/song.html', {'posts':posts})

    

class SongDetail(generic.DetailView):
    model = Testimony
    # #full_song == post_detail
    template_name = 'ushindi_app/full_song.html'


def gallery_album(request):
    posts = Album.objects.all()
    return render(request, 'ushindi_app/gallery_cover.html', {'posts':posts})
 

def album_view(request, id):
    album = get_object_or_404(Album, id=id)
    photos = GalleryPics.objects.filter(album=album)
    # # context = {
    # #     'post':post,
    # #     'photos':photos
    # # }

    return render(request, 'ushindi_app/gallery_pics.html', { 
        'album':album,
        'photos':photos
    })


def albums(request):

    # return render(request, 'app_ushindi/albums.html')
    pass 


def projects(request):


    posts = Projects.objects.all().order_by('-created_on')

    return render(request, 'ushindi_app/projects.html', {'posts':posts})




# def projects(request):

#     # # posts = BlogPost.objects.all()
#     # posts = Projects.objects.all().order_by('-created_on')

#     # return render(request, 'ushindi_app/projects.html', {'posts':posts})

#     pass 

class ProjectDetail(generic.DetailView):
    # model = Projects
    # #full_song == post_detail
    # template_name = 'app_ushindi/proj_detail.html'

    pass 

def proj_view(request, id):
    # album = get_object_or_404(Projects, id=id)
    # photos = ProjectPics.objects.filter(album=album)
    

    # return render(request, 'app_ushindi/proj_detail.html', {
    #     'album':album,
    #     'photos':photos,
        
    # })

    pass
