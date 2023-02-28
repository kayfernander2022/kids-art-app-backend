from django.shortcuts import render
from .models import ArtPiece
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ArtPieceSerializer, ImagekitAuthSerializer
from imagekitio import ImageKit
from rest_framework.response import Response
from rest_framework.views import APIView
from django.test import TestCase
from kidsartapp.settings import IMAGEKIT_KEY

# Create your views here.

class ArtPieceViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = ArtPiece.objects.all()
    # The serializer class for serializing output
    serializer_class = ArtPieceSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]
    
class imagekitAuthTest():
    
    def __init__(self,token,expire,signature,created=None): 

        self.token = token
        self.expire = expire
        self.signature = signature
   
class ImagekitAuth(APIView): 
    def get(self, request):
        imagekit = ImageKit(
            private_key=IMAGEKIT_KEY,
            public_key='public_33FjszinEBzlgrIz8+HbC3JVASM=',
            url_endpoint='https://ik.imagekit.io/jfpi8d5c5')

        auth_params = imagekit.get_authentication_parameters()
        
        token = list(auth_params.values())[0]
        expire = list(auth_params.values())[1]
        signature = list(auth_params.values())[2]
        
        data_obj = imagekitAuthTest(token,expire,signature)
        serializer_class = ImagekitAuthSerializer(data_obj)
        
        return Response(serializer_class.data)   
    

#handling the users request to auth against imagekit by giving a authentication token.