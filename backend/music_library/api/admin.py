from django.contrib import admin

from api.resources import SongResource, AlbumResource
from .models import Album, Song, Playlist
from import_export.admin import ImportExportModelAdmin

# class ArtistAdmin(ImportExportModelAdmin):
#     resource_classes = [ArtistResource]
# admin.site.register(Artist, ArtistAdmin)

class SongAdmin(ImportExportModelAdmin):
    resource_classes = [SongResource]
admin.site.register(Song, SongAdmin)

class AlbumAdmin(ImportExportModelAdmin):
    resource_classes = [AlbumResource]
admin.site.register(Album, AlbumAdmin)

admin.site.register(Playlist)
    

