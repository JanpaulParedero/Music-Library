from dataclasses import field
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from .models import Song, Album

# These resource classes allow Django to import csv files that contain the attributes needed for a schema

# INSERT INTO api_song (songURI, album, name, duration_ms, explicit, song_preview, track_number) VALUES (
#   'spotify:track:098ttCNmncrO4YvqWUNMvn', 
#   'spotify:album:2noRn2Aes5aoNVsU6iWThc',	
#   'High Life',
#   '201800',
#   'FALSE'
#   'https://p.scdn.co/mp3-preview/64de0035d909feff5e99481f4cec66dca4f75102?cid=9950ac751e34487dbbe027c4fd7f8e99'
#   '8');
class SongResource(resources.ModelResource):
    songURI = fields.Field(attribute='songURI', column_name='Track URI')
    album = fields.Field(widget = ForeignKeyWidget(Album, field='albumURI'), attribute='album', column_name='Album URI')
    name = fields.Field(attribute = 'name', column_name= 'Track Name')
    duration_ms = fields.Field(attribute = 'duration_ms', column_name= 'Track Duration (ms)')
    explicit = fields.Field(attribute='explicit', column_name= 'Explicit')
    song_preview = fields.Field(attribute='song_preview', column_name='Track Preview URL')
    track_number = fields.Field(attribute='track_number', column_name='Track Number')
    artists = fields.Field(attribute='artists', column_name='Artist Name(s)')
    
    class Meta:
        model = Song
        skip_unchanged = True
        import_id_fields = ('songURI',)
        fields = ('songURI','name', 'duration_ms', 'album', 'explicit', 'song_preview', 'track_number', 'artists')
        
# INSERT INTO api_album (albumURI, name, artist, release_date, cover_art) VALUES (
#   'spotify:album:2noRn2Aes5aoNVsU6iWThc', 
#   'Discovery', 
#   'Daft Punk', 
#   '2001-03-12', 
#   'https://i.scdn.co/image/ab67616d0000b273b33d46dfa2635a47eebf63b2');
class AlbumResource(resources.ModelResource):
    albumURI = fields.Field(attribute='albumURI', column_name='Album URI')
    name = fields.Field(attribute='name', column_name='Album Name')
    artist = fields.Field(attribute ='artist', column_name='Album Artist Name(s)')
    release_date = fields.Field(attribute='release_date', column_name='Album Release Date')
    cover_art = fields.Field(attribute='cover_art', column_name= 'Album Image URL')

    class Meta:
        model = Album
        skip_unchanged = True
        import_id_fields = ('albumURI',)
        fields = ('albumURI','name', 'artist', 'release_date','cover_art')
