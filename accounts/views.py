from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from .models import CustomUser 

class Create(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login') 
    template_name = 'registration/create.html'
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = str(form.cleaned_data['student_number'])
        
        if form.cleaned_data['user_type'] == 'admin':
            user.is_superuser = True
            user.is_staff = True 
        user.save() 
        return super().form_valid(form)