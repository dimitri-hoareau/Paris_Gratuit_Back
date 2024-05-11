from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import DrinkingFountain
from .serializers import DrinkingFountainSerializer

class DrinkingFountainViewSet(ReadOnlyModelViewSet):
    queryset = DrinkingFountain.objects.all()
    serializer_class = DrinkingFountainSerializer
