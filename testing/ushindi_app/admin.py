from django.contrib import admin
from .models import *


class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'singer', 'status', 'body', 'created_on')
    search_fields = ['title', 'singer', 'body', 'status']

admin.site.register(Testimony, SongAdmin)

class GalleryPicsAdmin(admin.StackedInline):
    model = GalleryPics

@admin.register(Album)

class PostAdmin(admin.ModelAdmin):
    inlines = [GalleryPicsAdmin]

    class Meta:
        model = Album

@admin.register(GalleryPics)

class GalleryPicsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Projects)
