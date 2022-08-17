from django.contrib import admin
from .models import *

# Register your models here.

class GalleryPosterAdmin(admin.ModelAdmin):

    list_display = ('title', 'content')

admin.site.register(GalleryPoster, GalleryPosterAdmin)
