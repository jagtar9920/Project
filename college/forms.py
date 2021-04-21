from django import forms
from .models import Appointment

class appointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment 
        fields = "__all__"