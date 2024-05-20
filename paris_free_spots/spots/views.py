from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import DrinkingFountain, Sanisette, WifiSpot, LabHIV
from .serializers import DrinkingFountainSerializer, SanisetteSerializer, WifiSpotSerializer, LabHIVSerializer

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