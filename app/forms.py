from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, ClinicVisit


class ClinicVisitForm(forms.ModelForm):
    
    class Meta:
        model = ClinicVisit
        fields = ('user', 'first_name', 'last_name', 'date', 'time_in', 'complaints', 'medical_intervention', 'remarks')