from django.contrib import admin
from .models import *

# Register your models here.

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'singer', 'status', 'body', 'created_on')
    search_fields = ['title', 'singer', 'body', 'status']

admin.site.register(Testimony, SongAdmin)

class AlbumPicsAdmin(admin.StackedInline):
    model = AlbumPics

@admin.register(Album)

class PostAdmin(admin.ModelAdmin):
    inlines = [AlbumPicsAdmin]

    class Meta:
        model = Album

@admin.register(AlbumPics)

class AlbumPicsAdmin(admin.ModelAdmin):
    pass