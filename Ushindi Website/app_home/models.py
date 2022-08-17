from turtle import title
from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Profile(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    about_me = models.TextField()

    def __str__(self):
        return self.author

class SongPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.CharField(default=True, max_length=110)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)
    date_edit = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'profile_image', null=True, blank=True)

    def __str__(self):
        return f"{self.author} Song of the Promised Land: {self.title} {self.date_created.year}/{self.date_created.month}/{self.date_created.day} "



class TestimonyPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.CharField(default=False, max_length=110)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'profile_image', null=True, blank=True)

    class Meta:
        ordering = ['-date_created']
    
    def __str__(self):
        return self.title