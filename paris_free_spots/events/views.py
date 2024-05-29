from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Event
from .serializers import EventSerializer

class EventViewSet(ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
