from .models import ArtPiece
from rest_framework import serializers

# Our ArtPieceSerializer
class ArtPieceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = ArtPiece
        # choose the fields that should be included in the serialized output we get back,which ones you want
        fields = ['id', 'title', 'description', 'image_url']


#the seralizers job is to give us pretty objects