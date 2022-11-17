from rest_framework import serializers
from .models import Song, Album, Playlist
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['songURI', 'name', 'artists', 'duration_ms', 'explicit', 'song_preview', 'track_number']

class AlbumSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many = True)
    class Meta:
        model = Album
        fields = ['albumURI','name', 'artist', 'release_date','cover_art', 'songs']

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'
        read_only_fields = ["user"]

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


