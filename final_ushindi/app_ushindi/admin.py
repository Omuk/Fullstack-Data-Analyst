from django.contrib import admin
from .models import *


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


class ProjectPicsAdmin(admin.StackedInline):
    model = ProjectPics

@admin.register(Projects)

class PostAdminProj(admin.ModelAdmin):
    inlines = [ProjectPicsAdmin]

    class Meta:
        model=Projects 
        
@admin.register(ProjectPics)

class ProjectPicsAdmin(admin.ModelAdmin):
    pass


# class ProjAdmin(admin.StackedInline):
#     model = ProjDetails

# @admin.register(ProjEvents)

# class ProjPostAdmin(admin.ModelAdmin):
#     inlines = [ProjAdmin]

#     class Meta:
#         model = ProjEvents

# @admin.register(ProjDetails)

# class ProjAdmin(admin.ModelAdmin):
#     pass

