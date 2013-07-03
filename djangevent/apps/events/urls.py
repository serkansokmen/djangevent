from django.conf.urls import *
from .views import (
    EventList,
)


urlpatterns = patterns(
    '',
    url(r'^$', EventList.as_view(), name='event_list'),
)
