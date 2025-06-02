from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from django.views import generic
from .models import ClinicVisit, Inventory, MedicalRecord


class DashboardPageView(TemplateView):
    template_name = "app/dashboard.html"


class ClinicVisitListView(ListView):
    model = ClinicVisit
    context_object_name = "clinicvisits"
    template_name = "app/clinicvisit_list.html"
    ordering = ['-date', '-time_in']


class ClinicVisitDetailView(DetailView):
    model = ClinicVisit
    context_object_name = "clinicvisit"
    template_name = "app/clinicvisit_detail.html"
    
class ClinicVisitCreateView(CreateView):
    model = ClinicVisit
    fields = ['date', 'time_in', 'user','complaints', 'medical_intervention', 'remarks']
    template_name = "app/clinicvisit_create.html" 

class InventoryListView(ListView):
    model = Inventory
    template_name = "app/inventory_list.html"


class MedicalRecordListView(ListView):
    model = MedicalRecord
    template_name = "app/medicalrecord_list.html"
