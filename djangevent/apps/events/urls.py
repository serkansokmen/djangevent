from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from .views import (
    EventCreate,
    ApiEventListCreate, ApiEventRetrieveUpdateDestroy
)


urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='events.html'), name='events'),
    url(r'^new/$', EventCreate.as_view(template_name='event_form.html'), name='event_form'),

    (r'^api/$', ApiEventListCreate.as_view()),
    (r'^api/(?P<pk>\d+)/$', ApiEventRetrieveUpdateDestroy.as_view()),
)
