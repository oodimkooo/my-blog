from django.forms import ModelForm, TextInput, DateInput
from .models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title','description','startDate','endDate']

        widgets = {
            'title': TextInput(attrs={'class': 'event-form', 'required': 'true'}),
            'description': TextInput(attrs={'class': 'event-form', 'required': 'true'}),
            'startDate': DateInput(attrs={'class': 'event-form'}),
            'endDate': DateInput(attrs={'class': 'event-form'}),
        }
