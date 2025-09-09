
from django import forms
from django.contrib.auth import get_user_model
from .models import Appointment
User = get_user_model()

class AppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(queryset=User.objects.filter(role='DOCTOR'), label='Doctor')
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type':'time'}))
    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time', 'service']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }