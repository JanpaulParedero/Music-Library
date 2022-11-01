from api.models import Album
from api.serializers import AlbumSerializer

def run():
    test_obj = Album.objects.get(pk='spotify:album:0ETFjACtuP2ADo6LFhL6HN')
    test_serializer = AlbumSerializer(instance=test_obj)
    print(test_serializer.data)