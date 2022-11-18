from django.urls import path
from .import views
from .views import AlbumDetailView, AlbumView, MyTokenObtainPairView, PlaylistDetailView, PlaylistView, RegisterView, SongDetailView, SongView, GenreView, ArtistView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.urlpatterns import format_suffix_patterns
app_name ='api'

urlpatterns = [

    path('', views.getRoutes),
    path('playlists/', PlaylistView.as_view()),
    path('playlists/<int:pk>/', PlaylistDetailView.as_view()),
    path('songs/', SongView.as_view(), name="songsApi"),
    path('songs/<str:pk>/', SongDetailView.as_view()),
    path('albums/', AlbumView.as_view(), name="albumApi"),
    path('genres/', GenreView.as_view(), name="genreApi"),
    path('artists/', ArtistView.as_view(), name="artistApi"),
    path('albums/<str:pk>', AlbumDetailView.as_view()),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view()),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)