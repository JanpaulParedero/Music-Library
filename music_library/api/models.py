from dataclasses import field
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Artist(models.Model):
    artistURI = models.CharField(max_length=255, primary_key=True)
    name = models.TextField()

    def __str__(self):
        return self.name 

class Album(models.Model):
    albumURI = models.CharField(max_length = 255, primary_key = True)
    name = models.TextField()
    artists = models.ManyToManyField(Artist, related_name='albums')
    release_date = models.DateField(null = True)
    cover_art = models.TextField(null = True)

    def __str__(self):
        return self.name 
        
class Genre(models.Model):
    genre_type = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.genre_type

class Song(models.Model):
    songURI = models.CharField(max_length = 255, primary_key=True)
    name = models.TextField()
    duration_ms = models.IntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, to_field='albumURI', related_name='songs')
    explicit = models.BooleanField(null = True)
    song_preview = models.TextField()
    track_number = models.IntegerField()
    artists = models.ManyToManyField(Artist)
    genres = models.ManyToManyField(Genre, related_name='songs')
 
    def __str__(self):
        return self.name

class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 255)
    songs = models.ManyToManyField(Song, blank=True)

    def __str__(self):
        return self.name
