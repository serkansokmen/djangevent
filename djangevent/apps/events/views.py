from .models import Event
from .serializers import EventSerializer
from rest_framework import generics


class EventList(generics.ListCreateAPIView):
    """
    List or Create Events
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventRetrieve(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update or Destroy Event
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
