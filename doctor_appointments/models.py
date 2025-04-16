from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=400, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone_number = models.CharField(
        max_length=30,
        blank=True,
        validators=[RegexValidator(r'^[\d\-\(\)\s]+$', 'Phone number must only contain numbers, spaces, dashes, or parentheses.')])
    preferred_contact = models.CharField(default=None, max_length=200)

    def __str__(self):
        return self.full_name


class Location(models.Model):
    city = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.city


class Specialisation(models.Model):
    specialisation_name = models.CharField(blank=True)

    def __str__(self):
        return self.specialisation_name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    full_name = models.CharField(max_length=400, blank=True)
    practice_name = models.CharField(max_length=400, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone_number = models.CharField(
        max_length=30, 
        blank=True, 
        validators=[RegexValidator(r'^[\d\-\(\)\s]+$', 'Phone number must only contain numbers, spaces, dashes, or parentheses.')])

    specialisations = models.ManyToManyField(Specialisation, related_name='doctors')
    locations = models.ManyToManyField(Location, related_name='doctors')
    address = models.CharField(max_length=200, blank=True)
    features = models.CharField(blank=True, max_length=400)

    def __str__(self):
        return self.full_name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_specialisation = models.ForeignKey(
        Specialisation, on_delete=models.CASCADE, default=1)
    doctor_location = models.ForeignKey(Location, on_delete=models.CASCADE, default=1)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    additional_info = models.TextField(default=None)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Add UniqueConstraint to ensure combination of doctor and appointment_date is unique
        # This allows a specific date & time appointment for each doctor to be only booked once
        constraints = [
            models.UniqueConstraint(fields=['doctor', 'appointment_date'], name='unique_appointment')
        ]

    def __str__(self):
        return f"{self.patient.full_name} at {self.doctor.practice_name} on {self.appointment_date}"
