import csv
from api.models import Song, Album

def run():
    file = open('api/Song_List.csv')
    read_file = csv.reader(file)

    Album.objects.all().delete()
    Song.objects.all().delete()
    

    # id = Artist.objects.only('id').get(name='The Beatles').id
    # print(id)
    
    # count = 1
    # for line in read_file:
    #     try:
    #         if count == 1:
    #             pass
    #         else: 
    #             Artist.objects.create(name = line[3])
    #             Album.objects.create(name = line[4],genre = line[2], artist = Artist.objects.only('id').get(name=line[3]).id, duration_min = line[5], release_year = line[6], cover_art = line[7]  )
    #             Song.objects.create(name = line[0], duration_sec = line[1], genre = line[2], artist = Artist.objects.only('id').get(name=line[3]).id, album = Artist.objects.only('id').get(name=line[4]).id)
    #         count += 1
    #     except Exception:
    #         pass
    
   