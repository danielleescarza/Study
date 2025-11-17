from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ("username", "email", "first_name", "last_name", "user_type", "is_staff", "is_active")
    list_filter = ("user_type", "is_staff", "is_active")

    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "user_type", "department", "level", "student_number")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "first_name", "last_name", "user_type", "department", "level", "student_number", "password1", "password2", "is_staff", "is_active"),
        }),
    )

    search_fields = ("email", "username", "first_name", "last_name")
    ordering = ("email",)

admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
