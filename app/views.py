from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from .models import ClinicVisit, Inventory, MedicalRecord
from accounts.models import CustomUser
from django.db.models import Q
import datetime


class DashboardPageView(TemplateView):
    template_name = "app/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get today's date uwu
        today = datetime.date.today()

        # Count the number of clinic visits for today uwu
        visit_count = ClinicVisit.objects.filter(date=today).count()

        # Count the total number of users uwu
        total_users = CustomUser.objects.count()  # Count total users

        # Count the number of inventory items near expiration (e.g., within the next 30 days) uwu
        expiration_threshold = today + datetime.timedelta(days=30)
        near_expiration_count = Inventory.objects.filter(
            expiration_date__lte=expiration_threshold, expiration_date__isnull=False
        ).count()

        # Add the visit count, current date, total users, and near expiration count to the context uwu
        context["visit_count"] = visit_count
        context["current_date"] = today  # Add current date to context
        context["total_users"] = total_users  # Add total users to context
        context["near_expiration_count"] = (
            near_expiration_count  # Add near expiration count to context
        )

        return context


class ClinicVisitListView(ListView):
    model = ClinicVisit
    context_object_name = "clinicvisits"
    template_name = "app/clinicvisit_list.html"
    ordering = ["-date", "-time_in"]

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("search_query")

        if search_query:
            queryset = queryset.filter(
                Q(user__student_number__icontains=search_query)
                | Q(user__first_name__icontains=search_query)
                | Q(user__last_name__icontains=search_query)
                | Q(user__department__icontains=search_query)
                | Q(complaint__icontains=search_query)
                | Q(medical_intervention__icontains=search_query)
            ).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("search_query", "")
        return context


class ClinicVisitDetailView(DetailView):
    model = ClinicVisit
    context_object_name = "clinicvisit"
    template_name = "app/clinicvisit_detail.html"


class ClinicVisitCreateView(CreateView):
    model = ClinicVisit
    fields = [
        "date",
        "time_in",
        "user",
        "complaint",
        "medical_intervention",
        "remarks",
    ]
    template_name = "app/clinicvisit_create.html"
    success_url = reverse_lazy("clinicvisits")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = CustomUser.objects.all()
        return context


class ClinicVisitUpdateView(UpdateView):
    model = ClinicVisit
    fields = [
        "date",
        "time_in",
        "user",
        "complaint",
        "medical_intervention",
        "remarks",
    ]
    template_name = "app/clinicvisit_update.html"
    success_url = reverse_lazy("clinicvisits")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = CustomUser.objects.all()
        return context


class ClinicVisitDeleteView(DeleteView):
    model = ClinicVisit
    template_name = "app/clinicvisit_delete.html"
    success_url = reverse_lazy("clinicvisits")


class MedicalRecordListView(ListView):
    model = MedicalRecord
    context_object_name = "medicalrecords"
    template_name = "app/medicalrecord_list.html"
    ordering = ["-date_recorded"]


class MedicalRecordDetailView(DetailView):
    model = MedicalRecord
    context_object_name = "medicalrecord"
    template_name = "app/medicalrecord_detail.html"


class MedicalRecordCreateView(CreateView):
    model = MedicalRecord
    fields = [
        "user",
        "date_recorded",
        "birth_date",
        "age",
        "sex",
        "residence",
        "fathers_name",
        "fathers_home_address",
        "fathers_contact_number",
        "mothers_name",
        "mothers_home_address",
        "mothers_contact_number",
        "primarycontact_name",
        "primarycontact_number",
        "medication_allergies",
        "food_allergies",
        "other_allergies",
        "severeallergic_reaction",
        "asthma_history",
        "carries_inhaler",
        "illness",
        "illness_age",
        "other_illness",
        "hospitalization_details",
        "wears_eyeglasses_or_contacts",
        "eye_vision_problem",
        "eye_vision_description",
        "hearing_problems",
        "hearing_description",
        "permission",
        "exception",
        "signature",
        "verification",
    ]
    template_name = "app/medicalrecord_create.html"
    success_url = reverse_lazy("medicalrecords")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = CustomUser.objects.all()
        return context


class MedicalRecordUpdateView(UpdateView):
    model = MedicalRecord
    fields = [
        "date_recorded",
        "birth_date",
        "age",
        "sex",
        "residence",
        "fathers_name",
        "fathers_home_address",
        "fathers_contact_number",
        "mothers_name",
        "mothers_home_address",
        "mothers_contact_number",
        "primarycontact_name",
        "primarycontact_number",
        "medication_allergies",
        "food_allergies",
        "other_allergies",
        "severeallergic_reaction",
        "asthma_history",
        "carries_inhaler",
        "illness",
        "illness_age",
        "other_illness",
        "hospitalization_details",
        "wears_eyeglasses_or_contacts",
        "eye_vision_problem",
        "eye_vision_description",
        "hearing_problems",
        "hearing_description",
        "exception",
        "signature",
        "signature",
        "verification",
    ]
    template_name = "app/medicalrecord_update.html"
    success_url = reverse_lazy("medicalrecords")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = CustomUser.objects.all()
        return context


class MedicalRecordDeleteView(DeleteView):
    model = MedicalRecord
    template_name = "app/medicalrecord_delete.html"
    success_url = reverse_lazy("medicalrecords")


class InventoryListView(ListView):
    model = Inventory
    context_object_name = "inventorys"
    template_name = "app/inventory_list.html"
    ordering = ["-arrival_date"]


class InventoryDetailView(DetailView):
    model = Inventory
    context_object_name = "inventory"
    template_name = "app/inventory_detail.html"


class InventoryCreateView(CreateView):
    model = Inventory
    fields = [
        "inventory_type",
        "description",
        "quantity",
        "unit",
        "arrival_date",
        "expiration_date",
        "remarks",
    ]
    template_name = "app/inventory_create.html"
    success_url = reverse_lazy("inventory")


class InventoryUpdateView(UpdateView):
    model = Inventory
    fields = [
        "inventory_type",
        "description",
        "quantity",
        "unit",
        "arrival_date",
        "expiration_date",
        "remarks",
    ]
    context_object_name = "inventorys"
    template_name = "app/inventory_update.html"
    success_url = reverse_lazy("inventory")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["inventory"] = self.object
        return context


class InventoryDeleteView(DeleteView):
    model = Inventory
    template_name = "app/inventory_delete.html"
    success_url = reverse_lazy("inventory")
