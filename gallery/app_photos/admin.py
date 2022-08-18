import os
import uuid
import zipfile
import photos.settings
from datetime import datetime
from zipfile import ZipFile

from django.contrib import admin
from .models import *
from .forms import *

from django.core.files.base import ContentFile

from PIL import Image

# Register your models here.

# @admin.register(Album)

class GalleryPosterAdmin(admin.ModelAdmin):

    list_display = ('title', 'content')


admin.site.register(GalleryPoster, GalleryPosterAdmin)

class NewAlbumAdmin(admin.ModelAdmin):

    list_display = ('title', 'content', 'pic')

admin.site.register(NewAlbums)


class AlbumModelAdmin(admin.ModelAdmin):
    form = AlbumForm
    
    list_display = ('title', 'content')


    def save_model(self, request, obj, form, change):
        if form.is_valid():
            album = form.save(commit=False)
            album.modified = datetime.now()
            album.save()

            if form.cleaned_data['zip'] != None:
                zip = zipfile.ZipFile(form.cleaned_data['zip'])
                for filename in sorted(zip.namelist()):

                    file_name = os.path.basename(filename)
                    if not file_name:
                        continue

                    data = zip.read(filename)
                    contentfile = ContentFile(data)

                    img = NewAlbums()
                    img.album = album
                    img.title = filename
                    filename = '{0}{1}.jpg'.format(album.title, str(uuid.uuid4())[-13:])
                    img.image.save(filename, contentfile)
                
                    filepath = '{0}/albums/{1}'.format(photos.settings.MEDIA_ROOT, filename)
                    with Image.open(filepath) as i:
                        img.width, img.height = i.size

                    img.pictur.save('thumb-{0}'.format(filename), contentfile)
                    img.save()
                zip.close() 
            super(AlbumModelAdmin, self).save_model(request, obj, form, change)

class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(AlbumImage)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = AlbumImage
@admin.register(PostImage)

class PostImageAdmin(admin.ModelAdmin):
    pass

# class GalleryModelAdmin(admin.ModelAdmin):
#     form = GalForm
    
#     list_display = ('title', 'content')


#     def save_model(self, request, obj, form, change):
#         if form.is_valid():
#             album = form.save(commit=False)
#             album.modified = datetime.now()
#             album.save()

#             if form.cleaned_data['zip'] != None:
#                 zip = zipfile.ZipFile(form.cleaned_data['zip'])
#                 for filename in sorted(zip.namelist()):

#                     file_name = os.path.basename(filename)
#                     if not file_name:
#                         continue

#                     data = zip.read(filename)
#                     contentfile = ContentFile(data)

#                     img = GalleryPoster()
#                     img.album
#                     img.title = filename
#                     filename = '{0}{1}.jpg'.format(album.title, str(uuid.uuid4())[-13:])
#                     img.image.save(filename, contentfile)
                
#                     filepath = '{0}/albums/{1}'.format(photos.settings.MEDIA_ROOT, filename)
#                     with Image.open(filepath) as i:
#                         img.width, img.height = i.size

#                     img.pictur.save('thumb-{0}'.format(filename), contentfile)
#                     img.save()
#                 zip.close() 
#             super(GalleryModelAdmin, self).save_model(request, obj, form, change)















