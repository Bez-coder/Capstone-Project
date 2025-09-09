
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Appointment(models.Model):
    STATUS_CHOICES = [('PENDING','Pending'),('CONFIRMED','Confirmed'),('CANCELLED','Cancelled')]
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_appointments')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_appointments')
    date = models.DateField()
    time = models.TimeField()
    service = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date','-time']

    def __str__(self):
        return f"{self.patient} -> {self.doctor} on {self.date} {self.time}"
