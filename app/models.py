from django.db import models
from django.urls import reverse_lazy
from django.conf import settings
import datetime


def current_time():
    return datetime.datetime.now().time()


# Clinic Visit Model
class ClinicVisit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    time_in = models.TimeField(default=current_time)
    complaints = models.TextField(blank=True)
    medical_intervention = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} {self.user.first_name} {self.user.last_name}"


class MedicalRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(default="", max_length=255)
    last_name = models.CharField(default="", max_length=255)
    department = models.CharField(default="", max_length=255)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


# Base abstract model for items with description, quantity, expiration_date, and remarks
class Inventory(models.Model):
    STATUS_CHOICES = [
        ('consumable_medicine', 'Consumable Medicine'),
        ('medical_supply', 'Medical Supply'),
        ('medical_instrument', 'Medical Instrument')
    ]

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='consumable_medicine')
    description = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    arrival_date = models.DateField(default=datetime.date.today)
    expiration_date = models.DateField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.status} - {self.description} - {self.quantity}"
