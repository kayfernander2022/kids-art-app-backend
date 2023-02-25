from django.db import models

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

# Create your models here.
class ArtPiece(models.Model):
    title = models.CharField(max_length=50, blank=False)
    # image_url = models.ImageField(null=True, blank=True, upload_to="images/")
    imageData = models.FileField()
    description = models.TextField(max_length=100)
