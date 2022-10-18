from xml.dom.pulldom import default_bufsize
from django.db import models

# Create your models here.
class Song(models.Model):
    name = models.TextField()
    artist = models.ForeignKey("Artist", on_delete=models.SET_NULL, null=True)
    duration_sec = models.IntegerField()
    genre = models.TextField()
    album = models.ForeignKey("Album", on_delete=models.SET_NULL, null=True)
    #playlist = models.ForeignKey("Playlist", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.TextField(unique = True, null = True)
    
    def __str__(self):
        return self.name 

class Album(models.Model):
    name = models.TextField(unique = True)
    genre = models.TextField()
    artist = models.ForeignKey("Artist", on_delete=models.SET_NULL, null=True)
    duration_min = models.IntegerField()
    release_year = models.IntegerField()
    cover_art = models.TextField(null = True)

    def __str__(self):
        return self.name + ' - ' + self.artist.name
    

class Playlist(models.Model):
    duration_min = models.IntegerField()
    creation_date = models.DateField()

    
