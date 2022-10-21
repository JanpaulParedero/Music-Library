
from django.http import Http404
from django.shortcuts import render
from .models import Album, Song
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AlbumSerializer, SongSerializer

def main(request):
    all_albums = Album.objects.all()
    return render(request, 'api/main.html', {'all_albums' : all_albums,})

def detail(request, albumURI):
    try:
        album = Album.objects.get(pk=albumURI)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'api/detail.html', {'album' : album})


class SongView(APIView):
    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many = True)
        return Response(serializer.data)
  
    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)

# class ArtistView(APIView):
#     def get(self, request):
#         artists = Artist.objects.all()
#         serializer = ArtistSerializer(artists, many = True)
#         return Response(serializer.data)
  
#     def post(self, request):
  
#         serializer = ArtistSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return  Response(serializer.data)

class AlbumView(APIView):
    serializer_class = AlbumSerializer
    def get(self, request):
        detail = [ {"id"    : detail.id,
                    "name"  : detail.name,
                    "songs": detail.songs,
                    "duration_min" : detail.duration_min,
                    "genre" : detail.genre,
                    "release_year" : detail.release_year,
                    "cover_art" : detail.cover_art} 

        for detail in Album.objects.all()]
        return Response(detail)
  
    def post(self, request):
  
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)