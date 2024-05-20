from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DrinkingFountainViewSet, SanisetteViewSet, WifiSpotViewSet

router = DefaultRouter()
router.register(r'drinking-fountains', DrinkingFountainViewSet)
router.register(r'sanisettes', SanisetteViewSet)
router.register(r'wifi-spots', WifiSpotViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
