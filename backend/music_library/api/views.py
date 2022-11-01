from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Album, Playlist, Song
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import AlbumSerializer, SongSerializer, PlaylistSerializer
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
# def main(request):
#     all_albums = Album.objects.all()
#     return render(request, 'api/main.html', {'all_albums' : all_albums,})

# def detail(request, albumURI):
#     album = get_object_or_404(Album, pk = albumURI)
#     return render(request, 'api/detail.html', {'album' : album})

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/token',
        'api/token/refresh',
    ]
    return Response(routes)

# class SongView(APIView):
#     serializer_class = SongSerializer

#     def get_queryset(self):
#         songs = Song.objects.all()
#         return songs

#     def get(self, request):
#         try:
#             songURI = request.query_params["songURI"]
#             if songURI != None:
#                 song = Song.objects.get(pk = songURI)
#                 serializer = SongSerializer(song)
#         except:
#             songs = Song.objects.all()
#             serializer = SongSerializer(songs, many = True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = SongSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return  Response(serializer.data)

class SongView(APIView):

    def get(self, request, format=None):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SongDetailView(APIView):

    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        songs = self.get_object(pk)
        serializer = SongSerializer(songs)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        songs = self.get_object(pk)
        serializer = SongSerializer(songs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        songs = self.get_object(pk)
        songs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class AlbumView(APIView):

    def get(self, request, format=None):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AlbumDetailView(APIView):
    
    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        albums = self.get_object(pk)
        serializer = AlbumSerializer(albums)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        albums = self.get_object(pk)
        serializer = AlbumSerializer(albums, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        albums = self.get_object(pk)
        albums.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# class AlbumView(APIView):
#     serializer_class = AlbumSerializer

#     def get_queryset(self):
#         albums = Album.objects.all()
#         return albums

#     def get(self, request):
#         try:
#             albumURI = request.query_params["albumURI"]
#             if albumURI != None:
#                 album = Album.objects.get(pk = albumURI)
#                 serializer = AlbumSerializer(album)
#         except:
#             albums = Album.objects.all()
#             serializer = AlbumSerializer(albums, many = True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = AlbumSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return  Response(serializer.data)


# @api_view(['GET'])
# def getPlaylist(self):
#         playlists = Playlist.objects.all()
#         serializer = PlaylistSerializer(playlists, many=True)
#         return Response(serializer.data)

# @api_view(['POST'])
# def postPlaylist(self,request):
#         serializer = PlaylistSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return  Response(serializer.data)

# class PlaylistView(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PlaylistSerializer
#     def get(self, request):
#         playlists = Playlist.objects.all()
#         serializer = PlaylistSerializer(playlists, many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer = PlaylistSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return  Response(serializer.data)

#     def put(self, request, pk):
#         try:
#             playlist= Playlist.objects.get(pk=pk)
#         except playlist.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         serializer = PlaylistSerializer(playlist, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return  Response(serializer.data)

class PlaylistView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        Playlists = Playlist.objects.all()
        serializer = PlaylistSerializer(Playlists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlaylistDetailView(APIView):
    permission_classes= [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Playlist.objects.get(pk=pk)
        except Playlist.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Playlists = self.get_object(pk)
        serializer = PlaylistSerializer(Playlists)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Playlists = self.get_object(pk)
        serializer = PlaylistSerializer(Playlists, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Playlists = self.get_object(pk)
        Playlists.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)