from rest_framework import viewsets
from api.models import Song
from api.serializers import SongSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset= Song.objects.all()
    serializer_class = SongSerializer
