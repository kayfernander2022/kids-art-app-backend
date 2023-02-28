from .models import ArtPiece
from rest_framework import serializers
from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions

# Our ArtPieceSerializer
class ArtPieceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = ArtPiece
        # choose the fields that should be included in the serialized output we get back,which ones you want
        fields = ['id', 'title', 'description', 'image_url']



class ImagekitAuthSerializer(serializers.Serializer):
    token = serializers.CharField()
    expire = serializers.CharField()
    signature = serializers.CharField()