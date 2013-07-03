from django.conf.urls import patterns, url
from django.views.generic import TemplateView, CreateView
from .views import (
    EventCreate,
    ApiEventList, ApiEventRetrieve
)


urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='events.html'), name='events'),
    url(r'^new/$', EventCreate.as_view(template_name='event_form.html'), name='event_form'),

    (r'^api/$', ApiEventList.as_view()),
    (r'^api/new/$', ApiEventRetrieve.as_view()),
)
