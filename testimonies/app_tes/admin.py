from django.contrib import admin
from .models import *

# Register your models here.

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'singer', 'status', 'body', 'created_on')
    search_fields = ['title', 'singer', 'body', 'status']

admin.site.register(Testimony, SongAdmin)