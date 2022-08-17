from django.shortcuts import render
from django.views import generic 
from .models import Testimony

# Create your views here.

def profile(request):

    # posts = BlogPost.objects.all()
    posts = Testimony.objects.all().order_by('-created_on')

    return render(request, 'app_tes/index.html', {'posts':posts})

# class Song(generic.ListView):
#     #song == queryset
#     #Testimony == Post
#     queryset = Testimony.objects.order_by('-created_on')
#     template_name = 'index.html'

class SongDetail(generic.DetailView):
    model = Testimony
    #full_song == post_detail
    template_name = 'app_tes/read_more.html'
