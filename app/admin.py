from django.contrib import admin
from .models import ClinicVisit, MedicalRecord, Inventory

admin.site.register(ClinicVisit)
admin.site.register(MedicalRecord)
admin.site.register(Inventory)

# Register your models here.
