# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 21:38:14 2021

@author: ksaik
"""

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Song, Audiobook, Podcast
from .serilalizers import songSerializer, audiobookSerializer, podcastSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

class audioPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

class audioList(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = songSerializer
    pagination_class = audioPagination
    
        

# class audioCreate(CreateAPIView):
#     serializer_class = songSerializer
#     queryset = Song.objects.all()
#     # def create(self, request, *args, **kwargs):
#     #     try:
#     #         data = request.data
#     #         name = self.request.data.get('name_of_the_song')
#     #         uploaded_time = self.request.data.get('uploaded_time')
#     #         if not name:
#     #             raise ValidationError('past dates are not accepted')
#     #     except ValueError:
#     #         raise ValidationError('String literals are only accepted')
#     #     return super().create(self, request, *args, **kwargs)
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
#     # def create(self,request, *args, **kwargs):
#     #     serializer = self.get_serializer(data=request.data)
    
    
    
class songRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    lookup_field = 'id'
    serializer_class = songSerializer
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)
    
        

    
@api_view(['GET'])
def audioAll(request, audioFileType):
    if audioFileType.lower() == 'song':
        song = Song.objects.all()
        serializer = songSerializer(song, many = True)
        return Response(serializer.data)
    elif audioFileType.lower() == 'audiobook':
        audiobook = Audiobook.objects.all()
        serializer = audiobookSerializer(audiobook, many=True)
        return Response(serializer.data)
    elif audioFileType.lower() == 'podcast':
        podcast = Podcast.objects.all()
        serializer = podcastSerializer(podcast, many=True)
        return Response(serializer.data)
    
    
@api_view(['GET'])
def audioDetails(request, id,audioFileType):
    if audioFileType.lower() == 'song':
        song = Song.objects.get(id = id)
        serializer = songSerializer(song)
        return Response(serializer.data)
    elif audioFileType.lower() == 'audiobook':
        audiobook = Audiobook.objects.get(id = id)
        serializer = audiobookSerializer(audiobook)
        return Response(serializer.data)
    elif audioFileType.lower() == 'podcast':
        podcast = Podcast.objects.get(id = id)
        serializer = podcastSerializer(podcast)
        return Response(serializer.data)
    


@api_view(['POST'])
def audioCreate(request, audioFileType):
    if audioFileType.lower() == 'song':
        song = Song.objects.all()
        serializer = songSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif audioFileType.lower() == 'audiobook':
        audiobook = Audiobook.objects.all()
        serializer = audiobookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif audioFileType.lower() == 'podcast':
        podcast = Podcast.objects.all()
        serializer = podcastSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    
@api_view(['POST'])
def audioUpdate(request, id, audioFileType):
    if audioFileType.lower() == 'song':
        song = Song.objects.get(id = id)
        serializer = songSerializer(instance= song, data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif audioFileType.lower() == 'audiobook':
        audiobook = Audiobook.objects.get(id = id)
        serializer = audiobookSerializer(instance= audiobook, data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif audioFileType.lower() == 'podcast':
        podcast = Podcast.objects.get(id = id)
        serializer = podcastSerializer(instance= podcast, data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
        
@api_view(['DELETE'])
def audioDelete(request, id, audioFileType):
    if audioFileType.lower() == 'song':
        song = Song.objects.get(id = id)
        song.delete()
        return Response("200 successfully deleted")
    elif audioFileType.lower() == 'audiobook':
        audiobook = Audiobook.objects.get(id = id)
        audiobook.delete()
        return Response("200 successfully deleted")
    elif audioFileType.lower() == 'podcast':
        podcast = Podcast.objects.get(id = id)
        podcast.delete()
        return Response("200 successfully deleted")    
        
        
    
    