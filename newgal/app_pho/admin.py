from django.contrib import admin
from .models import *

# Register your models here.

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


# # class AlbumAdmin(admin.ModelAdmin):
# #     list_display = ('title', 'content')

# admin.site.register(AlbumPicsAdmin, Album)

# class PostAdmin(admin.ModelAdmin):
#     inlines = [AlbumPicsAdmin]

#     class Meta:
#         model = Album

