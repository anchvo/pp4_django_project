from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Patients(models.Model):
    name = models.CharField(max_length=400)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=300)
    phone = models.IntegerField()
    password = models.CharField()
    preferred_contact = models.BooleanField()
    additional_info = models.TextField()
