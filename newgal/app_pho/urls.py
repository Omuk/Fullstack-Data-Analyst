from django.urls import path 
from app_pho.views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

   path('', views.album, name='blog'),
   path('<int:id>', views.album_view, name='detail')

    
   
] 

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
