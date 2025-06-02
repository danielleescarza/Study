from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('user_type', 'username', 'first_name', 'last_name', 'department', 'level', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('user_type', 'username', 'first_name', 'last_name', 'department', 'level')
        