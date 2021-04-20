# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 21:42:19 2021

@author: ksaik
"""

from rest_framework import serializers

from .models import Song, Podcast, Audiobook
#from .models import audiofiletype

class songSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('audiofiletype','id','name_of_the_song','duration_in_number_of_seconds', 'uploaded_time')
        
class audiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiobook
        fields = ('audiofiletype','id','title','author','narrator', 'duration_in_number_of_seconds', 'uploaded_time')
        
class podcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ('audiofiletype','id','duration_in_number_of_seconds', 'uploaded_time', 'name_of_the_podcast', 'host', 'participants')
    
