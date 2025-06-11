from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ClinicVisit, Inventory
from accounts.models import CustomUser


class ClinicVisitForm(forms.ModelForm):
    class Meta:
        model = ClinicVisit
        fields = ('user', 'date', 'time_in', 'complaint', 'medical_intervention', 'remarks')


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ('inventory_type', 'description', 'quantity', 'unit', 'arrival_date', 'expiration_date', 'remarks')
