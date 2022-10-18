from django.urls import path, re_path
from .import views

urlpatterns = [
    path('', views.main, name ='main'), 

    re_path(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]