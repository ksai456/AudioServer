from django.contrib import admin
from .models import  Song, Audiobook, Podcast
# Register your models here.

@admin.register(Song)
class songAdmin(admin.ModelAdmin):
    list_display = ['name_of_the_song', 'duration_in_number_of_seconds', 'uploaded_time']
    
@admin.register(Audiobook)
class audiobookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'narrator', 'duration_in_number_of_seconds', 'uploaded_time']
    
@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ['name_of_the_podcast', 'host', 'participants', 'duration_in_number_of_seconds', 'uploaded_time']