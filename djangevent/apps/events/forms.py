from django import forms
from .models import Event
from html5.forms.widgets import DateInput, TimeInput


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        exclude = ('owner',)
        widgets = {
            'name': forms.TextInput(attrs={
                'ng-model': 'event.name',
                'required': 'required',
            }),
            'date': DateInput(attrs={
                'ng-model': 'event.date',
                'show-weeks': 'showWeeks',
                'required': 'required',
            }),
            'time': TimeInput(attrs={
                'ng-model': 'event.time',
                'required': 'required',
            }),
            'location': forms.TextInput(attrs={'ng-model': 'event.location'}),
            'image': forms.TextInput(attrs={'ng-model': 'event.image'}),
        }
