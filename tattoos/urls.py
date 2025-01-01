from rest_framework import routers
from django.urls import path, include
from .views import TattoosImgMultiparser

router = routers.DefaultRouter()
router.register('TattoosImgMultiparser', TattoosImgMultiparser)

urlpatterns = [
    path('', include(router.urls)),
]