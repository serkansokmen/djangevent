from django.views.generic import CreateView
from .models import Event
from .serializers import EventSerializer
from rest_framework import generics


class ApiEventList(generics.ListCreateAPIView):
    """
    List or Create Events
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ApiEventRetrieve(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update or Destroy Event
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventCreate(CreateView):
    model = Event
    template_name = 'event_form.html'
