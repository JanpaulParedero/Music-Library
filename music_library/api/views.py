
from django.http import Http404
from django.shortcuts import render
from .models import Album, Song, Artist


def main(request):
    all_albums = Album.objects.all()
    return render(request, 'api/main.html', {'all_albums' : all_albums,})

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'api/detail.html', {'album' : album})