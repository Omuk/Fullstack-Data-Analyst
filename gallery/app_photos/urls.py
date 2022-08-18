# from . import views
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from app_photos.views import *

from django.contrib.auth import views
from django.views.generic.base import RedirectView

from django.conf import settings


from . import forms 
from .import views

from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
   path('ind/', views.gallery, name='gallery'),
   # path('<int:pk>/', AlbumDetail.as_view(), name='album'), #app.views.AlbumView.as_view()
   # path('<int:pk>/', GalleryDetailView.as_view(), name='albumm'), #app.views.AlbumView.as_view()
   path('<int:pk>/', BlogDetailView.as_view(), name='album'),

   path('', views.blog_view, name='blog'),
   path('<int:id>', views.detail_view, name='detail')

    
   
] 

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

