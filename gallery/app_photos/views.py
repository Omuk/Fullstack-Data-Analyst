from django.shortcuts import render,get_object_or_404
from django.views import generic

from .forms import PostForm
from .models import *
from django.http import HttpRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView

# Create your views here.

def gallery(request):
    posts = GalleryPoster.objects.all()

    return render(request, 'app_photos/index.html', {'posts':posts})

# class GalleryDetailView(generic.DetailView):
#     model = GalleryPoster
#     template_name= 'app_photos/album.html'

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super(GalleryDetailView, self).get_context_data(**kwargs)
#         # Add in a QuerySet of all the images
#         context['images'] = GalleryPoster.objects.filter(pictr=self.object.id)
#         return context


# class AlbumDetail(DetailView):
class BlogDetailView(generic.DetailView):
    model = GalleryPoster
    template_name= 'app_photos/blog_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the images
        context['images'] = NewAlbums.objects.filter(album=self.object.id)
        return context

    # template_name= 'app_photos/blog_detail.html'
    


def blog_view(request):
    posts = AlbumImage.objects.all()
    return render(request, 'app_photos/blog.html', {'posts':posts})

def detail_view(request, id):
    post = get_object_or_404(AlbumImage, id=id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'app_photos/detail.html', {
        'post':post,
        'photos':photos
    })



