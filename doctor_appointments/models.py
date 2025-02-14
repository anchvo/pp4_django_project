from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=400, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone_number = models.IntegerField(default=None)
    preferred_contact = models.BooleanField(default=None)

    def __str__(self):
        return self.user.username


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    full_name = models.CharField(max_length=400, blank=True)
    practice_name = models.CharField(max_length=400, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone_number = models.IntegerField(default=None)
    specialisation = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    features = models.BooleanField(default=None)

    def __str__(self):
        return self.user.username


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    additional_info = models.TextField(default="Medication Plan:")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} at {self.doctor} on {self.appointment_date}"
