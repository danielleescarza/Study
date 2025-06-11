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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(default="", max_length=255)
    last_name = models.CharField(default="", max_length=255)
    department = models.CharField(default="", max_length=255)

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
