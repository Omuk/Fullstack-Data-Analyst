from django.contrib import admin
from django.urls import path
from app_ushindi.views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orphanhome', views.orphanhome, name='orphanhome'),
    path('ics', views.ics, name='ics'),
    path('high', views.high, name='high'),
    path('', views.projects, name='projects'),
    # path('<int:id>', views.album_view, name='detail')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)