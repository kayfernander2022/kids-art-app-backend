"""kidsartapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from kidsart.views import ArtPieceViewSet

# create a new router
router = routers.DefaultRouter()
# register our viewsets with the router
router.register(r'kidsart', ArtPieceViewSet) #register "/todos" routes #r makes it a raw string //this is creating an array of paths

urlpatterns = [
     # add all of our router urls
    path('', include(router.urls)),#any url, got to router
    path('admin/', admin.site.urls),
]
