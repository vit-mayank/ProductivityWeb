from django import forms
from .models import events

class EventCreationForm(forms.ModelForm):
    class Meta:
        model = events
        fields = ['title','desc','event_date','category']
        widgets = {
            'event_date':forms.DateInput(attrs={'type':'date'})
        }
        