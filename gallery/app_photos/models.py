from email.policy import default
from django.db import models

# Create your models here.


class GalleryPoster (models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    gal_pos = models.ImageField(default='default.jpg', upload_to='gal_poster')
    pic = models.ImageField(default='default.jpg', upload_to='all_kids')
    # pic = models.ImageField(default='default.jpg', upload_to='small_kids')
    # pic = models.ImageField(default='default.jpg', upload_to='older_kids')
    # pic = models.ImageField(default='default.jpg', upload_to='projects')
    # pic = models.ImageField(default='default.jpg', upload_to='high')

    def __str__(self):
        return self.title