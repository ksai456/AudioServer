from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Song
from .models import Audiobook
from .models import Podcast
# from .models import audiofiletype
# Create your views here.

def home(request):
    songs = Song.objects.all()
    audiobooks = Audiobook.objects.all()
    podcasts = Podcast.objects.all()
    return render(request, 'home.html',{'songs':songs, 'audiobooks': audiobooks, 'podcasts':podcasts})


def song_details(request, id):
    try:
        song = Song.objects.get(id = id)
    except Song.DoesNotExist:
        raise Http404('song not found')
    return render(request, 'song_details.html', {'song':song,})
        
    

def audiobook_details(request, id):
    try:
        audiobook = Audiobook.objects.get(id = id)
    except Audiobook.DoesNotExist:
        raise Http404('audiobook not found')
    return render(request, 'audiobook_details.html', {'audiobook':audiobook,})


def podcast_details(request, id):
    try:
        podcast = Podcast.objects.get(id = id)
    except Podcast.DoesNotExist:
        raise Http404('podcast not found')
    return render(request, 'podcast_details.html', {'podcast':podcast,})


# def audio_details(request, id, audioFileType):
#     if audioFileType:
#         if audioFileType.lower() == "song":
#             try:
#                 song = Song.objects.get(id = id, audiofiletype = audioFileType)
#             except Song.DoesNotExist:
#                 raise Http404('song not found')
#             return render(request, 'song_details.html', {'song':song,'audiofiletype':audioFileType,})
#         elif audioFileType.lower() == "audiobook":
#             try:
#                 audiobook = Audiobook.objects.get(id = id)
#             except Audiobook.DoesNotExist:
#                 raise Http404('audiobook not found')
#             return render(request, 'audiobook_details.html', {'audiobook':audiobook,'audiofiletype':audioFileType,})
#         else:
#             try:
#                 podcast = Podcast.objects.get(id = id)
#             except Podcast.DoesNotExist:
#                 raise Http404('podcast not found')
#             return render(request, 'podcast_details.html', {'podcast':podcast,'audiofiletype':audioFileType,})