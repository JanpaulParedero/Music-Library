from django.contrib import admin
from django.urls import path, include
#from api.views import SongView, AlbumView , ArtistView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # path('songs/', SongView.as_view(), name="songsApi"),
    # path('artists/', ArtistView.as_view(), name="artistsApi"),
    # path('album/', AlbumView.as_view(), name="albumApi"),
    
]