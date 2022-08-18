from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.

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
