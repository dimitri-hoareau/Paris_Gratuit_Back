from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import DrinkingFountain, Sanisette, WifiSpot
from .serializers import DrinkingFountainSerializer, SanisetteSerializer, WifiSpotSerializer

class DrinkingFountainViewSet(ReadOnlyModelViewSet):
    queryset = DrinkingFountain.objects.all()
    serializer_class = DrinkingFountainSerializer

class SanisetteViewSet(ReadOnlyModelViewSet):
    queryset = Sanisette.objects.all()
    serializer_class = SanisetteSerializer

class WifiSpotViewSet(ReadOnlyModelViewSet):
    queryset = WifiSpot.objects.all()
    serializer_class = WifiSpotSerializer
