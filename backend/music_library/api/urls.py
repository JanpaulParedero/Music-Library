from django.urls import path
from .import views
from .views import AlbumDetailView, AlbumView, MyTokenObtainPairView, PlaylistDetailView, PlaylistView, SongDetailView, SongView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.urlpatterns import format_suffix_patterns
app_name ='api'

urlpatterns = [
    #path('', views.main, name ='main'), 
    #path('<albumURI>', views.detail, name = 'detail'),

    path('', views.getRoutes),
    #path('playlists/', views.getPlaylist),
    #path('playlists/', PlaylistView.as_view(), name="playlistApi"),
    path('playlists/', PlaylistView.as_view()),
    path('playlists/<int:pk>/', PlaylistDetailView.as_view()),
    path('songs/', SongView.as_view(), name="songsApi"),
    path('songs/<str:pk>/', SongDetailView.as_view()),
    path('albums/', AlbumView.as_view(), name="albumApi"),
    path('albums/<str:pk>', AlbumDetailView.as_view()),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)