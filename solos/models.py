from django.db import models

# Create your models here.
class Solo(models.Model):
    track = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    instrument = models.CharField(max_length=50)
    album=models.CharField(max_length=200)
    start_time = models.CharField(max_length=20, blank=True, null=True)
    end_time = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return f"Track: {self.track}, Artist: {self.artist}"