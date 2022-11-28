from django.http import Http404
from .models import Album, Song, Playlist, Genre, Artist
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import AlbumSerializer, AlbumDetailSerializer ,SongSerializer, SongDetailSerializer, PlaylistSerializer,PlaylistDetailSerializer, RegisterSerializer, UserSerializer, GenreSerializer, GenreDetailSerializer, ArtistSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/token',
        'api/token/refresh',
    ]
    return Response(routes)

class GenreView(APIView):

    def get(self, request, format=None):
        #genres = Genre.objects.all()
        genres = Genre.objects.raw('SELECT * FROM public.api_genre ORDER BY id ASC ')
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GenreDetailView(APIView):

    def get_object(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        genres = self.get_object(pk)
        serializer = GenreDetailSerializer(genres)
        return Response(serializer.data)
        

class ArtistView(APIView):

    def get(self, request, format=None):
        #artists = Artist.objects.all()
        artists = Artist.objects.raw('SELECT * FROM public.api_artist')
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SongView(APIView):

    def get(self, request, format=None):
        #songs = Song.objects.all()
        songs = Song.objects.raw('SELECT * FROM public.api_song')
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
        serializer = SongDetailSerializer(songs)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        songs = self.get_object(pk)
        serializer = SongDetailSerializer(songs, data=request.data)
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
        albums = Album.objects.raw('SELECT * FROM public.api_album')
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
        serializer = AlbumDetailSerializer(albums)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        albums = self.get_object(pk)
        serializer = AlbumDetailSerializer(albums, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        albums = self.get_object(pk)
        albums.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlaylistView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        Playlists = Playlist.objects.filter(user = request.user)
        serializer = PlaylistSerializer(Playlists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlaylistDetailView(APIView):
    permission_classes= [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Playlist.objects.get(pk=pk, user = self.request.user)
        except Playlist.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Playlists = self.get_object(pk)
        serializer = PlaylistDetailSerializer(Playlists)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        Playlist = self.get_object(pk)
        serializer = PlaylistSerializer(Playlist, data=request.data)
        if serializer.is_valid():
            serializer.save(user = self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Playlists = self.get_object(pk)
        Playlists.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlaylistDetailSimpleView(APIView):
    permission_classes= [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Playlist.objects.get(pk=pk, user = self.request.user)
        except Playlist.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Playlists = self.get_object(pk)
        serializer = PlaylistSerializer(Playlists)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        Playlist = self.get_object(pk)
        serializer = PlaylistSerializer(Playlist, data=request.data)
        if serializer.is_valid():
            serializer.save(user = self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Playlists = self.get_object(pk)
        Playlists.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



