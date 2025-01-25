from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DrinkingFountainViewSet, SanisetteViewSet, WifiSpotViewSet, LabHIVViewSet, DefibrillateurViewSet, OrganicWasteTrashViewSet, RecyclingTrashViewSet, TextileRecyclingTrashViewSet, SecondLifeCenterViewSet, SapinCollectViewSet

router = DefaultRouter()
router.register(r'drinking-fountains', DrinkingFountainViewSet)
router.register(r'sanisettes', SanisetteViewSet)
router.register(r'wifi-spots', WifiSpotViewSet)
router.register(r'lab-hiv', LabHIVViewSet)
router.register(r'defibrillateur', DefibrillateurViewSet)
router.register(r'organic-waste-trash', OrganicWasteTrashViewSet)
router.register(r'glass-recycling-trash', RecyclingTrashViewSet)
router.register(r'textile-recycling-trash', TextileRecyclingTrashViewSet)
router.register(r'second-life-centers', SecondLifeCenterViewSet)
router.register(r'sapin-collect', SapinCollectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
