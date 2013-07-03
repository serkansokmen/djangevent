from django.shortcuts import get_object_or_404
from .models import Event
from .serializers import EventSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response


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
