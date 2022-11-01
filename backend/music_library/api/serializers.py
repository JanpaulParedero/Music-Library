from rest_framework import serializers
from .models import Song, Album, Playlist

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


