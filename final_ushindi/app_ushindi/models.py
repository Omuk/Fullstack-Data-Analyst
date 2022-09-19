from turtle import title
from django.db import models
from django.contrib.auth.models import User
from distutils.command.upload import upload

# Create your models here.

STATUS = ( 
    ('Alumni', 'Alumni'),
    ('Current Child', 'Current Child')
)

class Testimony(models.Model):
    title = models.CharField(max_length=200)
    singer = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    # image = models.ImageField(upload_to='images', null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')
    # vids = models.FileField(upload_to='videos', default=False)
    status = models.CharField(max_length=13, choices=STATUS, default='Alumni')


    class Meta :
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title

class Album(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.FileField(default='default.jpg', upload_to='album_prof')

    def __str__(self):
        return self.title 


class AlbumPics(models.Model): 
    album = models.ForeignKey(Album, on_delete=models.CASCADE, default=None)
    images = models.FileField(upload_to='pics')

    def __str__(self):
        return self.album.title
        # return self.album.title

eventchoices = (
    ('Previous', 'Previous'),
    ('Current', 'Current'),
    ('Future', 'Future')
)


class ProjEvents(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.FileField(default='default.jpg', upload_to='proj_pic')
    status = models.CharField(max_length=113, choices=eventchoices, default='Current')

    def __str__(self):
        return self.title 

class ProjDetails(models.Model): 

    album = models.ForeignKey(ProjEvents, on_delete=models.CASCADE, default=None)
    content = models.TextField(default=False)
    images = models.FileField(upload_to='pics')

    def __str__(self):
        return self.album.title
        # return self.album.title







































class PreviousProjects(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='proj_pic')
    status = models.CharField(max_length=113, choices=eventchoices, default='Current')

    def __str__(self):
        return self.title

class CurrentProjects(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='proj_pic')
    status = models.CharField(max_length=113, choices=eventchoices, default='Current')

    def __str__(self):
        return self.title 

class FutureProjects(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='proj_pic')
    status = models.CharField(max_length=113, choices=eventchoices, default='Current')

    def __str__(self):
        return self.title


