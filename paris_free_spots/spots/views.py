from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import DrinkingFountain, Sanisette, WifiSpot, LabHIV, Defibrillateur, OrganicWasteTrash, RecyclingTrash, TextileRecyclingTrash, SecondLifeCenter, SapinCollect
from .serializers import DrinkingFountainSerializer, SanisetteSerializer, WifiSpotSerializer, LabHIVSerializer, DefibrillateurSerializer, OrganicWasteTrashSerializer, RecyclingTrashSerializer, TextileRecyclingTrashSerializer, SecondLifeCenterSerializer, SapinCollectSerializer

class DrinkingFountainViewSet(ReadOnlyModelViewSet):
    queryset = DrinkingFountain.objects.all()
    serializer_class = DrinkingFountainSerializer

class SanisetteViewSet(ReadOnlyModelViewSet):
    queryset = Sanisette.objects.all()
    serializer_class = SanisetteSerializer

class WifiSpotViewSet(ReadOnlyModelViewSet):
    queryset = WifiSpot.objects.all()
    serializer_class = WifiSpotSerializer

class LabHIVViewSet(ReadOnlyModelViewSet):
    queryset = LabHIV.objects.all()
    serializer_class = LabHIVSerializer

class DefibrillateurViewSet(ReadOnlyModelViewSet):
    queryset = Defibrillateur.objects.all()
    serializer_class = DefibrillateurSerializer

class OrganicWasteTrashViewSet(ReadOnlyModelViewSet):
    queryset = OrganicWasteTrash.objects.all()
    serializer_class = OrganicWasteTrashSerializer

class RecyclingTrashViewSet(ReadOnlyModelViewSet):
    queryset = RecyclingTrash.objects.all()
    serializer_class = RecyclingTrashSerializer

class TextileRecyclingTrashViewSet(ReadOnlyModelViewSet):
    queryset = TextileRecyclingTrash.objects.all()
    serializer_class = TextileRecyclingTrashSerializer

class SecondLifeCenterViewSet(ReadOnlyModelViewSet):
    queryset = SecondLifeCenter.objects.all()
    serializer_class = SecondLifeCenterSerializer

class SapinCollectViewSet(ReadOnlyModelViewSet):
    queryset = SapinCollect.objects.all()
    serializer_class = SapinCollectSerializer