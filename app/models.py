from django.db import models
from django.urls import reverse_lazy
from django.conf import settings
import datetime


def current_time():
    return datetime.datetime.now().time()


class ClinicVisit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    time_in = models.TimeField(default=current_time)
    complaint = models.TextField(max_length=30, blank=True, default="")
    medical_intervention = models.TextField(max_length=30, blank=True, default="")
    remarks = models.TextField(max_length=30, blank=True, default="")

    def __str__(self):
        return f"{self.date} {self.user.first_name} {self.user.last_name}"


class MedicalRecord(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    RESIDENCE_CHOICES = [
        ('both', 'Both Parents'),
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('guardian', 'Guardian'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_recorded = models.DateField(default=datetime.date.today)
    birth_date = models.DateField(blank=False, null=False)
    age = models.PositiveBigIntegerField(null=False, blank=False)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default="M")
    residence = models.CharField(max_length=100, choices=RESIDENCE_CHOICES, default="both")
    # Father's Information
    fathers_name = models.CharField(max_length=100, default="")
    fathers_home_address = models.TextField(default="")
    fathers_contact_number = models.CharField(max_length=15, default="")
    # Mother's Information
    mothers_name = models.CharField(max_length=100, default="")
    mothers_home_address = models.TextField(default="")
    mothers_contact_number = models.CharField(max_length=15, default="")
    # Primary Contact's Information
    primarycontact_name = models.CharField(max_length=100, default="")
    primarycontact_number = models.CharField(max_length=15, default="")
    # Allergies
    medication_allergies = models.TextField(blank=True)
    food_allergies = models.TextField(blank=True)
    other_allergies = models.TextField(blank=True)
    severeallergic_reaction = models.BooleanField(default=False)
    # Asthma
    asthma_history = models.BooleanField(default=False)
    carries_inhaler = models.BooleanField(default=False)
    # Conditions with age of diagnosis
    diabetes_age = models.PositiveIntegerField(null=True, blank=True)
    meningitis_age = models.PositiveIntegerField(null=True, blank=True)
    tuberculosis_age = models.PositiveIntegerField(null=True, blank=True)
    pneumonia_age = models.PositiveIntegerField(null=True, blank=True)
    heart_disorder_age = models.PositiveIntegerField(null=True, blank=True)
    urinary_disorder_age = models.PositiveIntegerField(null=True, blank=True)
    epilepsy_age = models.PositiveIntegerField(null=True, blank=True)
    scoliosis_age = models.PositiveIntegerField(null=True, blank=True)
    psoriasis_age = models.PositiveIntegerField(null=True, blank=True)
    vitiligo_age = models.PositiveIntegerField(null=True, blank=True)
    atopic_dermatitis_age = models.PositiveIntegerField(null=True, blank=True)
    impetigo_age = models.PositiveIntegerField(null=True, blank=True)
    other_conditions = models.TextField(blank=True)
    # Hospitalization Information
    hospitalization_details = models.TextField(blank=True)
    # Eye Problems
    wears_eyeglasses_or_contacts = models.BooleanField(default=False)
    eye_vision_problem = models.BooleanField(default=False)
    eye_vision_description = models.TextField(blank=True)
    # Ear Problems
    hearing_problems = models.BooleanField(default=False)
    hearing_description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


class Inventory(models.Model):
    INVENTORY_TYPE_CHOICES = [
        ('consumable_medicine', 'Consumable Medicine'),
        ('medical_supply', 'Medical Supply'),
        ('medical_instrument', 'Medical Instrument')
    ]

    inventory_type = models.CharField(max_length=50, choices=INVENTORY_TYPE_CHOICES, default='consumable_medicine')
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    unit = models.CharField(max_length=255, default="")
    arrival_date = models.DateField(default=datetime.date.today)
    expiration_date = models.DateField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.inventory_type} - {self.description} - {self.quantity}"
