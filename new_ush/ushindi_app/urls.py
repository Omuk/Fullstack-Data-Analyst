from django.contrib import admin
from django.urls import path
from ushindi_app.views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orphanhome', views.orphanhome, name='orphanhome'),
    path('ics', views.ics, name='ics'),
    path('high', views.high, name='high'),
    path('involved', views.involved, name='involved'),
    path('projects', views.projects, name='projects'),
    path('song', views.song, name='song'),
    path('album', views.gallery_album, name='album'),

    path('mem_pics', views.mem_view, name='mem_detail'),
    path('agr_pics', views.agr_view, name='agr_detail'),
    path('alum_pics', views.alum_view, name='alum_detail'),
    path('beg_pics', views.beg_view, name='beg_detail'),
    path('cul_pics', views.cul_view, name='cul_detail'),
    path('exc_pics', views.exc_view, name='exc_detail'),
    path('high_pics', views.high_view, name='high_detail'),

    path('inter_pics', views.inter_view, name='inter_detail'),
    path('kid_pics', views.kid_view, name='kid_detail'),
    path('mom_pics', views.mom_view, name='mom_detail'),
    path('sol_pics', views.sol_view, name='sol_detail'),
    
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)