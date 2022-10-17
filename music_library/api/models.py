from django.db import models

# Create your models here.
class Song(models.Model):
    name = models.TextField()
    artist = models.ForeignKey("Artist", on_delete=models.SET_NULL, null=True)
    duration_sec = models.IntegerField()
    genre = models.TextField()
    album = models.ForeignKey("Album", on_delete=models.SET_NULL, null=True)
    playlist = models.ForeignKey("Playlist", on_delete=models.SET_NULL, null=True)

class Artist(models.Model):
    name = models.TextField()

class Album(models.Model):
    name = models.TextField()
    genre = models.TextField()
    artist = models.ForeignKey("Artist", on_delete=models.SET_NULL, null=True)
    duration_min = models.IntegerField()
    release_year = models.IntegerField()
    

class Playlist(models.Model):
    duration_min = models.IntegerField()
    creation_date = models.DateField()


