from rest_framework import routers
from django.urls import path, include
from .views import PiercingsImgMultiparser

router = routers.DefaultRouter()
router.register('PiercingsImgMultiparser', PiercingsImgMultiparser)

urlpatterns = [
    path('', include(router.urls)),
]