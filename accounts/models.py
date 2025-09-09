
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    DOCTOR = 'DOCTOR'
    PATIENT = 'PATIENT'
    ROLE_CHOICES = [(DOCTOR, 'Doctor'), (PATIENT, 'Patient')]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=PATIENT)

    def is_doctor(self):
        return self.role == self.DOCTOR
