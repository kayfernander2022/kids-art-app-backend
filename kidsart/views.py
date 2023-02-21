from django.shortcuts import render
from .models import ArtPiece
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ArtPieceSerializer

# Create your views here.
#we dont have to define all the routes like we previously did we just need this viewset. it will create all the index, update, show,delete routes

class ArtPieceViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = ArtPiece.objects.all()
    # The serializer class for serializing output
    serializer_class = ArtPieceSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]
    
    
    
    
#now do the router in urls.py