from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from accounts.models import CustomUser
from app.models import Inventory, ClinicVisit, MedicalRecord

class Command(BaseCommand):
    help = "Seed groups and permissions"

    def handle(self, *args, **kwargs):
        groups = {
            "admin": {
                "permissions": [
                    "add_customuser", "change_customuser", "delete_customuser", "view_customuser",
                    "add_inventory", "change_inventory", "delete_inventory", "view_inventory",
                    "add_clinicvisit", "change_clinicvisit", "delete_clinicvisit", "view_clinicvisit",
                    "add_medicalrecord", "change_medicalrecord", "delete_medicalrecord", "view_medicalrecord",
                ]
            },
            "employee": {
                "permissions": [
                    "view_customuser",
                    "add_inventory", "change_inventory", "view_inventory",
                    "add_medicalrecord", "change_medicalrecord", "view_medicalrecord",
                    "view_clinicvisit",
                ]
            },
            "student": {
                "permissions": [
                    "view_inventory",
                    "view_clinicvisit",
                ]
            }
        }

        for group_name, data in groups.items():
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created group: {group_name}"))
            else:
                self.stdout.write(f"Group {group_name} already exists")

            # Clear existing permissions
            group.permissions.clear()

            # Assign permissions
            model_app_map = {
                "customuser": "accounts",
                "inventory": "app",
                "clinicvisit": "app",
                "medicalrecord": "app",
            }

            for codename in data["permissions"]:
                model_name = codename.split("_", 1)[1]  # e.g., "add_inventory" -> "inventory"
                app_label = model_app_map.get(model_name)
                if not app_label:
                    self.stdout.write(self.style.WARNING(f"No app_label found for {codename}"))
                    continue
                try:
                    perm = Permission.objects.get(codename=codename, content_type__app_label=app_label)
                    group.permissions.add(perm)
                    self.stdout.write(f"  Added permission {codename} to {group_name}")
                except Permission.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"Permission {codename} not found"))

        self.stdout.write(self.style.SUCCESS("Groups and permissions seeding completed."))