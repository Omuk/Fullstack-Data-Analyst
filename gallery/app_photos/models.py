from turtle import title
import uuid
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


from email.policy import default
from django.db import models

# Create your models here.


class GalleryPoster (models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    gal_pos = models.ImageField(default='default.jpg', upload_to='gal_poster')
    # pictr = models.ImageField(default='default.jpg', upload_to='all_pics')
    # pictr1 = models.ImageField(default='default.jpg', upload_to='all_pics')
    # pictr2 = models.ImageField(default='default.jpg', upload_to='all_pics')
    # pictr3 = models.ImageField(default='default.jpg', upload_to='all_pics')
    # pictr4 = models.ImageField(default='default.jpg', upload_to='all_pics')
    alt = models.CharField(max_length=255, default=uuid.uuid4)

    def __str__(self):
        return self.title


class NewAlbums(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    album = models.ForeignKey(GalleryPoster,on_delete=models.CASCADE)
    pictur = models.ImageField(default='default.jpg', upload_to='all_pics')
    pictur1 = models.ImageField(default='default.jpg', upload_to='all_pics')
    pictur2 = models.ImageField(default='default.jpg', upload_to='all_pics')
    pictur3 = models.ImageField(default='default.jpg', upload_to='all_pics')
    pictur4 = models.ImageField(default='default.jpg', upload_to='all_pics')
    pictur5 = models.ImageField(default='default.jpg', upload_to='all_pics')
    pictur6 = models.ImageField(default='default.jpg', upload_to='all_pics')
    alt = models.CharField(max_length=255, default=uuid.uuid4)

    def __str__(self):
        return self.title



# class Albums(models.Model):
#     user = models.ForeignKey(User)
#     title = models.CharField(max_length=128)
#     body = models.CharField(max_length=400)

# def get_image_filename(instance, filename):
#     id = instance.post.id
#     return "post_images/%s" % (id)  


# class Images(models.Model):
#     album = models.ForeignKey(GalleryPoster,on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, default=None)
#     image = models.ImageField('upload_to=more_tries',
#                               verbose_name='Image')



# class PhotoGallery(models.Model):
#     albumpic = models.ForeignKey(GalleryPoster, on_delete=models.CASCADE, null=True, blank=False)
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     pic1 = models.ImageField(default='default.jpg', upload_to='Rafiki')
#     # pic1 = models.ImageField(default='default.jpg', upload_to='Rafiki')
#     # pic1 = models.ImageField(default='default.jpg', upload_to='Rafiki')

#     def __str__(self):
#         return self.title
        # return self.albumpic

#Upload_to for now its same image folder for all pictures, galposter is the profile picture folder....when you get more advanced then you can get technical

# class RafikiGallery(models.Model):
#     albumpi = models.ForeignKey(GalleryPoster, on_delete=models.CASCADE, null=True, blank=False)
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     pic2 = models.ImageField(default='default.jpg', upload_to='Rafiki')
#     # pic1 = models.ImageField(default='default.jpg', upload_to='Rafiki')
#     # pic1 = models.ImageField(default='default.jpg', upload_to='Rafiki')

#     def __str__(self):
#         return self.title

# class Picture(models.Model):
#     post = models.ForeignKey(GalleryPoster, on_delete=models.CASCADE, null=True, blank=False)
#     file = models.ImageField(default='default.jpg', upload_to='album')



# class Album(models.Model):
#     title = models.CharField(max_length=70)
#     description = models.TextField(max_length=1024)
#     thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(300)], format='JPEG', options={'quality': 90})
#     tags = models.CharField(max_length=250)
#     is_visible = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now_add=True)
#     slug = models.SlugField(max_length=50, unique=True)

#     #def get_absolute_url(self):
#     #    return reverse('album', kwargs={'slug':self.slug})

#     def __unicode__(self):
#         return self.title

# class AlbumImage(models.Model):
#     image = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(1280)], format='JPEG', options={'quality': 70})
#     thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(300)], format='JPEG', options={'quality': 80})
#     album = models.ForeignKey('album', on_delete=models.PROTECT)
#     alt = models.CharField(max_length=255, default=uuid.uuid4)
#     created = models.DateTimeField(auto_now_add=True)
#     width = models.IntegerField(default=0)
#     height = models.IntegerField(default=0)
#     slug = models.SlugField(max_length=70, default=uuid.uuid4, editable=False)

class AlbumImage(models.Model):
    title = models.CharField(max_length=200)
    descript = models.TextField()
    image = models.FileField(blank=True)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post =models.ForeignKey(AlbumImage, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='test/')

    def __str__(self):
        return self.post.title