from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orphanhome', views.orphanhome, name='orphanhome'),
    path('highschool', views.highschool, name='highschool'),
    path('intermountain', views.intermountain, name='intermountain'),
    path('song', views.song, name='song'),
    path('projects', views.projects, name='projects'),
]