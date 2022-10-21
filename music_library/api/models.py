from dataclasses import field
from django.db import models
# In Django, creating models creates tables in your database of choice. 
# It allows you to specify types and even add refernces to other tables. 
# These models translate the python code into SQL in order to be made in Postgresql

#   CREATE TABLE "api_album"(
    #   "albumURI" varchar(255) NOT NULL PRIMARY KEY, 
    #   "name" text NOT NULL, 
    #   "artist" text NOT NULL, 
    #   "release_date" date NULL, 
    #   "cover_art" text NULL);
class Album(models.Model):
    albumURI = models.CharField(max_length = 255, primary_key =True)
    name = models.TextField()
    artist = models.TextField("Artist")
    release_date = models.DateField(null = True)
    cover_art = models.TextField(null = True)

    def __str__(self):
        return self.name 

#   CREATE TABLE "api_song" (
    #   "songURI" varchar(255) NOT NULL PRIMARY KEY, 
    #   "name" text NOT NULL, 
    #   "duration_ms" integer NOT NULL, 
    #   "album" varchar(255) REFERENCES Album,
    #   "explicit" boolean NULL, 
    #   "song_preview" text NOT NULL, 
    #   "track_number" integer NOT NULL);
class Song(models.Model):
    songURI = models.CharField(max_length = 255, primary_key=True)
    name = models.TextField()
    duration_ms = models.IntegerField()
    album = models.ForeignKey("Album", on_delete=models.CASCADE, null=True, to_field='albumURI')
    explicit = models.BooleanField(null = True)
    song_preview = models.TextField()
    track_number = models.IntegerField()

    def __str__(self):
        return self.name