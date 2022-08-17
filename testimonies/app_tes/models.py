from telnetlib import STATUS
from django.db import models
from django.contrib.auth.models import User

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
    status = models.CharField(max_length=13, choices=STATUS, default='Alumni')


    class Meta :
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title


