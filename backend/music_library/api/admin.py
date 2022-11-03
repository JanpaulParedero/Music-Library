from django.contrib import admin

from api.resources import SongResource, AlbumResource
from .models import Album, Song, Playlist
from import_export.admin import ImportExportModelAdmin

class SongAdmin(ImportExportModelAdmin):
    resource_classes = [SongResource]
admin.site.register(Song, SongAdmin)

class AlbumAdmin(ImportExportModelAdmin):
    resource_classes = [AlbumResource]
admin.site.register(Album, AlbumAdmin)

class PlaylistAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
admin.site.register(Playlist)
    

