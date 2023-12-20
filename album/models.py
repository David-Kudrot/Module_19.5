from django.db import models
from musician.models import Musician

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=50)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, default=None, related_name='albums')
    album_release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.id} : {self.album_name} "