from rest_framework import serializers
from .models import  Album,  Artist, Song, Playlist, Genre
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'genre_type']

class AlbumSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many = True)
    class Meta:
        model = Album
        fields = ['albumURI','name', 'artists', 'release_date','cover_art']

class SongSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many = True)
    album = AlbumSerializer()
    class Meta:
        model = Song
        fields = ['songURI', 'name', 'artists', 'duration_ms', 'explicit', 'song_preview', 'track_number', 'album']

class SongDetailSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many = True)
    genres = GenreSerializer(many = True)
    album = AlbumSerializer()
    class Meta:
        model = Song
        fields = ['songURI', 'name', 'artists', 'duration_ms', 'explicit', 'song_preview', 'track_number', 'genres', 'album']

class GenreDetailSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)
    class Meta:
        model = Genre
        fields = ['id', 'genre_type', 'songs']

class AlbumDetailSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many = True)
    artists = ArtistSerializer(many = True)
    class Meta:
        model = Album
        fields = ['albumURI','name', 'artists', 'release_date','cover_art', 'songs']

class PlaylistSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)

    class Meta:
        model = Playlist
        fields = ['id', 'name','user','songs']
        read_only_fields = ["user"]
        depth = 0

class PlaylistDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    songs = SongSerializer(many=True)
    class Meta:
        model = Playlist
        fields = ['id', 'name','user','songs']
        read_only_fields = ["user"]
        
        
    def validate_stock_list(self, songs):
        existing_stock_list = []
        if self.instance and self.instance.songs:
            # Patch or Put request
            existing_stock_list = self.instance.songs
        return existing_stock_list + songs

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'last_name')
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user( 
                username = validated_data['username'],
                password = validated_data['password'] ,
                first_name = validated_data['first_name'],  
                last_name = validated_data['last_name'])
        return user


