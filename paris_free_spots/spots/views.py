from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import DrinkingFountain, Sanisette
from .serializers import DrinkingFountainSerializer, SanisetteSerializer

class DrinkingFountainViewSet(ReadOnlyModelViewSet):
    queryset = DrinkingFountain.objects.all()
    serializer_class = DrinkingFountainSerializer

class SanisetteViewSet(ReadOnlyModelViewSet):
    queryset = Sanisette.objects.all()
    serializer_class = SanisetteSerializer

