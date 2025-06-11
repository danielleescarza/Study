from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import DashboardPageView, ClinicVisitListView, ClinicVisitDetailView, ClinicVisitCreateView, \
    ClinicVisitUpdateView, ClinicVisitDeleteView, InventoryListView, InventoryDetailView, InventoryCreateView, \
    InventoryUpdateView, InventoryDeleteView, MedicalRecordListView

urlpatterns = [
    path('', DashboardPageView.as_view(), name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('clinicvisits/', ClinicVisitListView.as_view(), name='clinicvisits'),
    path('clinicvisits/<int:pk>/', ClinicVisitDetailView.as_view(), name='clinicvisits_detail'),
    path('clinicvisits/create', ClinicVisitCreateView.as_view(), name='clinicvisits_create'),
    path('clinicvisits/<int:pk>/update/', ClinicVisitUpdateView.as_view(), name='clinicvisits_update'),
    path('clinicvisits/<int:pk>/delete/', ClinicVisitDeleteView.as_view(), name='clinicvisits_delete'),
    path('inventory/', InventoryListView.as_view(), name='inventory'),
    path('inventory/<int:pk>/', InventoryDetailView.as_view(), name='inventory_detail'),
    path('inventory/create', InventoryCreateView.as_view(), name='inventory_create'),
    path('inventory/<int:pk>/update/', InventoryUpdateView.as_view(), name='inventory_update'),
    path('inventory/<int:pk>/delete/', InventoryDeleteView.as_view(), name='inventory_delete'),
    path('medicalrecords/', MedicalRecordListView.as_view(), name='medicalrecords'),
]
