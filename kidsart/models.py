from django.db import models

# Create your models here.
class ArtPiece(models.Model):
    title = models.CharField(max_length=50, blank=False)
    image_url = models.ImageField()
    description = models.TextField(max_length=100)
