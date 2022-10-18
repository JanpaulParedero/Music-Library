from django.contrib import admin
from .models import Album, Song, Artist
from import_export import resources

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Artist)


class AlbumResource(resources.ModelResource):
    class Meta:
        model = Album
        import_id_fields = ('id',)
        skip_unchanged = True
        report_skipped = False
        fields = ('name', 'genre', 'artist__id')

class ArtistResource(resources.ModelResource):
    class Meta:
        model = Artist

class SongResource(resources.ModelResource):
    class Meta:
        model = Song


