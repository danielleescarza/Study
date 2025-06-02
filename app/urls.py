from django.contrib import admin
from django.urls import path
from . import views
from .views import DashboardPageView, ClinicVisitListView, ClinicVisitDetailView, ClinicVisitCreateView, InventoryListView, MedicalRecordListView

urlpatterns = [
    path('', DashboardPageView.as_view(), name='dashboard'),
    path('clinicvisits/', ClinicVisitListView.as_view(), name='clinicvisits'),
    path('clinicvisits/<int:pk>/', ClinicVisitDetailView.as_view(), name='clinicvisits_detail'),
    path('clinicvisits/new', ClinicVisitCreateView.as_view(), name='clinicvisits_create'),
    path('inventory/', InventoryListView.as_view(), name='inventory'),
    path('medicalrecords/', MedicalRecordListView.as_view(), name='medicalrecords'),
]