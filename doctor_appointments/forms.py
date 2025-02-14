from django import forms
from .models import Role


class RoleForm(forms.ModelForm):
    CHOICES = (
        ('1', 'Patient'),
        ('2', 'Doctor'),
    )
    role = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = Role
        fields = ('role',)
