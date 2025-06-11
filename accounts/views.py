from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from .models import CustomUser


class Create(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/create.html"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = str(
            form.cleaned_data["student_number"]
        )  # Set username to student number

        # Set user permissions based on user type
        user_type = form.cleaned_data["user_type"]
        if user_type == "admin":
            user.is_superuser = True
            user.is_staff = True
        else:
            user.is_superuser = False
            user.is_staff = True

        user.save()  # Save the user instance
        return super().form_valid(form)
