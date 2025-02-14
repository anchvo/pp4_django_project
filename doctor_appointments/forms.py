from django import forms
from .models import Role, Patient, Doctor


class RoleForm(forms.ModelForm):
    CHOICES = (
        ('1', 'Patient'),
        ('2', 'Doctor'),
    )
    role = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = Role
        fields = ('role',)


class PatientProfileForm(forms.ModelForm):
    CHOICES = (
        ('1', 'Email'),
        ('2', 'Phone'),
    )
    full_name = forms.CharField(max_length=400, help_text="Please enter your first, middle and last name.")
    email = forms.EmailField(max_length=254, help_text="Please enter your email address.")
    phone_number = forms.IntegerField(help_text="Please enter your phone number.")
    preferred_contact = forms.ChoiceField(choices=CHOICES, help_text="Please let us know how you want to be contacted if something happens.")

    class Meta:
        model = Patient
        fields = ('full_name', 'email', 'phone_number', 'preferred_contact',)

