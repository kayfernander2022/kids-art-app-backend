from django.db import models

# Create your models here.
class ArtPiece(models.Model):
    title = models.CharField(max_length=50, blank=False)
    image_url = models.CharField(max_length=2000)
    # imageData = models.FileField()
    description = models.TextField(max_length=100)
