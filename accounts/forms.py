from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            "user_type",
            "uid",
            "student_number",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )

        def save(self, commit=True):
            user = super().save(commit=False)
            # Set the username to the student_number
            user.username = str(self.cleaned_data["student_number"])
            if commit:
                user.save()
            return user


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = (
            "user_type",
            "uid",
            "student_number",
            "first_name",
        )

        def save(self, commit=True):
            user = super().save(commit=False)
            # Set the username to the student_number
            user.username = str(self.cleaned_data["student_number"])
            if commit:
                user.save()
            return user
