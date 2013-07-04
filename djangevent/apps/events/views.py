from django.views.generic import CreateView
from .models import Event
from .forms import EventForm
from .serializers import EventSerializer
from rest_framework import generics


class ApiEventListCreate(generics.ListCreateAPIView):
    """
    List or Create Events
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ApiEventRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update or Destroy Event
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventCreate(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'event_form.html'
