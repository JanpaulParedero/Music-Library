from django import views
from django.contrib import admin
from django.urls import path, include, re_path
from api.views import SongView, AlbumView 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # path('songs/', SongView.as_view(), name="songsApi"),
    # path('albums/', AlbumView.as_view(), name="albumApi"),
    
]