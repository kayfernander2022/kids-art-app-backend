
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from kidsart.views import ArtPieceViewSet, ImagekitAuth
from django.conf.urls.static import static
from django.conf import settings

# create a new router
router = routers.DefaultRouter()
# register our viewsets with the router
router.register(r'kidsart', ArtPieceViewSet) #register "/kidsart" routes #r makes it a raw string //this is creating an array of paths

urlpatterns = [
     # add all of our router urls
    path('', include(router.urls)),#any url, got to router
    path('admin/', admin.site.urls),
    path('api/imagekit-auth', ImagekitAuth.as_view())
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#allow uploaded image to create a url


