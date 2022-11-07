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
    path('song', views.song, name='song'),
    path('projects', views.projects, name='projects'),
]
