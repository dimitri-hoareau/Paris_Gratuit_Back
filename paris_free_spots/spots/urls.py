from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DrinkingFountainViewSet, SanisetteViewSet, WifiSpotViewSet, LabHIVViewSet, DefibrillateurViewSet

router = DefaultRouter()
router.register(r'drinking-fountains', DrinkingFountainViewSet)
router.register(r'sanisettes', SanisetteViewSet)
router.register(r'wifi-spots', WifiSpotViewSet)
router.register(r'lab-hiv', LabHIVViewSet)
router.register(r'defibrillateur', DefibrillateurViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
