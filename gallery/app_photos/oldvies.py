from django.shortcuts import render
from django.views import generic
from .models import *
from django.http import HttpRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView

# Create your views here.


# def gallery(request):
#     list = Album.objects.filter(is_visible=True).order_by('-created')
#     paginator = Paginator(list, 10)

#     page = request.GET.get('page')
#     try:
#         albums = paginator.page(page)
#     except PageNotAnInteger:
#         albums = paginator.page(1) # If page is not an integer, deliver first page.
#     except EmptyPage:
#         albums = paginator.page(paginator.num_pages) # If page is out of range (e.g.  9999), deliver last page of results.

#     return render(request, 'app_photos/gallery.html', { 'albums': list })

def gallery(request):
    posts = GalleryPoster.objects.all()

    return render(request, 'app_photos/index.html', {'posts':posts})

# class AlbumDetail(DetailView):
#      model = Album

#      def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super(AlbumDetail, self).get_context_data(**kwargs)
#         # Add in a QuerySet of all the images
#         context['images'] = AlbumImage.objects.filter(album=self.object.id)
#         return context
    

class BlogDetailView(generic.DetailView):
    model = PhotoGallery

    
    template_name = 'app_photos/blog_detail.html'

def handler404(request, exception):
    assert isinstance(request, HttpRequest)
    return render(request, 'handler404.html', None, None, 404)




# def more_img(request, pk):

#     posts = GalleryPoster.objects.all(id=pk)
#     pics = PhotoGallery.objects.all(instance=posts)

#     context = {
#         'posts': posts,
#         'pics': pics
#     }

#     return render(request, 'app_photos/photo.html', context)