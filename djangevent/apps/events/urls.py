from django.conf.urls import patterns
from .views import (
    ApiEventListCreate, ApiEventRetrieveUpdateDestroy
)


urlpatterns = patterns(
    '',
    (r'^events/$', ApiEventListCreate.as_view()),
    (r'^events/(?P<pk>\d+)/$', ApiEventRetrieveUpdateDestroy.as_view()),
)
