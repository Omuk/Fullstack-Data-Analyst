from . import views 
# from app_tes.views import *
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    # path('', views.Song.as_view(), name='home'),
    path('', views.profile, name='profile'),
    path('<int:pk>/', views.SongDetail.as_view(), name='read_more')
]



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)