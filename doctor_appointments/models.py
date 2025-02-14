from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=400, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone_number = models.IntegerField(default=None)
    preferred_contact = models.CharField(default=None)

    def __str__(self):
        return self.full_name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    full_name = models.CharField(max_length=400, blank=True)
    practice_name = models.CharField(max_length=400, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone_number = models.IntegerField(default=None)
    specialisations = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    features = models.BooleanField(default=None)

    def __str__(self):
        return self.full_name


class Role(models.Model):
    role = models.CharField(default=None)

    def __str__(self):
        return self.role


class Location(models.Model):
    location = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.location.city


class Features(models.Model):
    features = models.CharField(default=None)

    def __str__(self):
        return self.features


class Specialisation(models.Model):
    specialisation = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.specialisation.specialisations


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_specialisation = models.ForeignKey(
        Specialisation, on_delete=models.CASCADE, default=1)
    doctor_location = models.ForeignKey(Location, on_delete=models.CASCADE, default=1)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    additional_info = models.TextField(default=None)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.full_name} at {self.doctor.practice_name} on {self.appointment_date}"
