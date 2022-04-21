from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import Artist, Music
from .serializers import (
    ArtistListSerializer,
    ArtistSerializer,
    MusicListSerializer,
    MusicSerializer,
)


# Create your views here.
@api_view(['GET', 'POST'])
def artist_list(request):

    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistListSerializer(artists, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArtistListSerializer(data=request.data)    # 사용자 요청 데이터 바인딩
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        # 생성된 데이터 응답
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)

    serializer = ArtistSerializer(artist)

    return Response(serializer.data)

@api_view(['POST'])
def artist_music(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    serializer = MusicListSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(artist=artist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicListSerializer(musics, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def music_detail(request, pk):
    music = get_object_or_404(Music, pk=pk)

    if request.method == 'GET':
        serializers = MusicSerializer(music)
        return Response(serializers.data)
    
    elif request.method == 'PUT':
        serializers = MusicSerializer(data=request.data, instance=music)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        music.delete()
        data = {
            'id' : f'{pk}'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)