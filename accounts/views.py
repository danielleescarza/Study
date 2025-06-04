from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from .models import CustomUser 

class Create(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')  # Redirect to the login page after successful creation
    template_name = 'registration/create.html'
    
    def form_valid(self, form):
        # Set the username to the student_number before saving
        user = form.save(commit=False)
        user.username = str(form.cleaned_data['student_number'])
        user.save()
        return super().form_valid(form)