from django.contrib import admin
from api.resources import  AlbumResource,  ArtistResource, SongResource, GenreResource
from .models import Album, Artist, Song, Genre, Playlist
from import_export.admin import ImportExportModelAdmin

class SongAdmin(ImportExportModelAdmin):
    resource_classes = [SongResource]
admin.site.register(Song, SongAdmin)

class AlbumAdmin(ImportExportModelAdmin):
    resource_classes = [AlbumResource]
admin.site.register(Album, AlbumAdmin)

class GenreAdmin(ImportExportModelAdmin):
    resource_classes = [GenreResource]
admin.site.register(Genre, GenreAdmin)

class ArtistAdmin(ImportExportModelAdmin):
    resource_classes = [ArtistResource]
admin.site.register(Artist, ArtistAdmin)

class PlaylistAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
admin.site.register(Playlist)
    

