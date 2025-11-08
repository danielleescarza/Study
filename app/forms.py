from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ClinicVisit, Inventory, MedicalRecord
from accounts.models import CustomUser


class ClinicVisitForm(forms.ModelForm):
    class Meta:
        model = ClinicVisit
        fields = ('user', 'date', 'time_in', 'complaint', 'medical_intervention', 'remarks')


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ('inventory_type', 'description', 'quantity', 'unit', 'arrival_date', 'expiration_date', 'remarks')


class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = [
            'user', 'date_recorded', 'birth_date', 'age', 'sex', 'residence',
            'fathers_name', 'fathers_home_address', 'fathers_contact_number',
            'mothers_name', 'mothers_home_address', 'mothers_contact_number',
            'primarycontact_name', 'primarycontact_number',
            'medication_allergies', 'food_allergies', 'other_allergies', 'severeallergic_reaction',
            'asthma_history', 'carries_inhaler',
            'illness', 'illness_age', 'other_illness',
            'hospitalization_details',
            'wears_eyeglasses_or_contacts', 'eye_vision_problem', 'eye_vision_description',
            'hearing_problems', 'hearing_description', 'signature','verification'
        ]