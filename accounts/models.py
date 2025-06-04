from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ("student", "Student"),
        ("employee", "Employee"),
        ("admin", "Admin"),
    )

    DEPARTMENT_CHOICES = (
        ("BED", "Basic Education Department"),
        ("BSN", "Bachelor of Science in Nursing"),
        ("BSCS", "Bachelor of Science in Computer Science"),
        ("BSA", "Bachelor of Science in Accountancy"),
        ("BSBA","Bachelor of Science in Business Administration Major in Operational Management"),
        ("BSP", "Bachelor of Science in Psychology"),
        ("BSRT", "Bachelor of Science in Radiologic Technology"),
        ("BSHM", "Bachelor of Science in Hospitality Management"),
        ("BEEd", "Bachelor of Science in Elementary Education"),
        ("BSEd-Filipino", "Bachelor of Science in Secondary Education Major in Filipino"),
        ("BSEd-English", "Bachelor of Science in Secondary Education Major in English"),
    )
    
    LEVEL_CHOICES = (
        ("first_year", "1st Year"),
        ("second_year", "2nd Year"),
        ("third_year", "3rd Year"),
        ("fourth_year","4th Year"),
    )

    user_type = models.CharField(
        max_length=10, choices=USER_TYPE_CHOICES, default="student"
    )
    uid = models.CharField(max_length=32, unique=True, null=True, blank=True)
    student_number = models.PositiveBigIntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    level = models.CharField(max_length=100, choices=LEVEL_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_number})"


# Create your models here.
