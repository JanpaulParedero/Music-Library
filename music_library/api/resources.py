from dataclasses import field
from import_export import fields, resources
from import_export.widgets import  ManyToManyWidget , ForeignKeyWidget
from .models import  Album,  Artist, Song, Genre

class ArtistResource(resources.ModelResource):
    artistURI = fields.Field(attribute='artistURI', column_name='artistURI')
    name= fields.Field(attribute='name', column_name='Artist Name')

    class Meta:
        model = Artist
        import_id_fields = ('artistURI',)
        skip_unchanged = True
        fields = '__all__'

class GenreResource(resources.ModelResource):
    id = fields.Field(attribute='pk', column_name='id')
    genre_type = fields.Field(attribute='genre_type', column_name='genre_type')

    class Meta:
        model = Genre
        import_id_fields = ('id',)
        skip_unchanged = True
        fields = ('id', 'genre_type')

class SongResource(resources.ModelResource):
    songURI = fields.Field(attribute='songURI', column_name='Track URI')
    album = fields.Field(widget = ForeignKeyWidget(Album, field='albumURI'), attribute='album', column_name='Album URI')
    name = fields.Field(attribute = 'name', column_name= 'Track Name')
    duration_ms = fields.Field(attribute = 'duration_ms', column_name= 'Track Duration (ms)')
    explicit = fields.Field(attribute='explicit', column_name= 'Explicit')
    song_preview = fields.Field(attribute='song_preview', column_name='Track Preview URL')
    track_number = fields.Field(attribute='track_number', column_name='Track Number')
    artists = fields.Field(
        attribute='artists', 
        column_name='Artist Name(s)',
        widget=ManyToManyWidget(Artist, field='name', separator=','))
    genres = fields.Field(
        attribute='genres', 
        column_name='Genres',
        widget=ManyToManyWidget(Genre, field='genre_type', separator=','))
    
    class Meta:
        model = Song
        skip_unchanged = True
        import_id_fields = ('songURI',)
        fields = ('songURI','name', 'duration_ms', 'explicit', 'album', 'song_preview', 'track_number', 'artists', 'genres')
        
class AlbumResource(resources.ModelResource):
    albumURI = fields.Field(attribute='albumURI', column_name='Album URI')
    name = fields.Field(attribute='name', column_name='Album Name')
    artists = fields.Field(
        attribute='artists', 
        column_name='Album Artist Name(s)',
        widget=ManyToManyWidget(Artist, field='name', separator=','))
    release_date = fields.Field(attribute='release_date', column_name='Album Release Date')
    cover_art = fields.Field(attribute='cover_art', column_name= 'Album Image URL')

    class Meta:
        model = Album
        skip_unchanged = True
        import_id_fields = ('albumURI',)
        fields = ('albumURI','name', 'artists', 'release_date','cover_art')

