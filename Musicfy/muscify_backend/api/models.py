from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='cover_img/')
    audio = models.FileField(upload_to='song_audio/')
    
    def __str__(self):
        return f"{self.title} by {self.artist}"
