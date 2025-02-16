from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django import forms
from .models import Patient, Doctor, Appointment, Location, Specialisation


# Patient Profile
class PatientProfileForm(forms.ModelForm):
    # Set validator for phone number to ensure correct format
    phone_number_validator = RegexValidator(
        r'^[\d\-\(\)\s]+$', 'Phone number must only contain numbers, spaces, dashes, or parentheses.')

    CHOICES = (
        ('Email', 'Email'),
        ('Phone', 'Phone'),
    )
    full_name = forms.CharField(
        max_length=400, help_text="Please enter your first, middle and last name.")
    email = forms.EmailField(
        max_length=254, help_text="Please enter your email address.")
    phone_number = forms.CharField(
        max_length=30,
        validators=[phone_number_validator], help_text="Please enter your phone number.")
    preferred_contact = forms.ChoiceField(
        choices=CHOICES, help_text="Please let us know how you want to be contacted if something happens.")

    class Meta:
        model = Patient
        fields = ('full_name', 'email', 'phone_number', 'preferred_contact',)


# Doctor Profile
class DoctorProfileForm(forms.ModelForm):
    # Set validator for phone number to ensure correct format
    phone_number_validator = RegexValidator(
        r'^[\d\-\(\)\s]+$', 'Phone number must only contain numbers, spaces, dashes, or parentheses.')

    OPTIONS = (
        ('Parking', 'Parking'),
        ('Elevator', 'Elevator'),
        ('Disabled Access', 'Disabled Access'),
    )
    title = forms.CharField(
        max_length=100, help_text="Please enter your medical title.")
    full_name = forms.CharField(
        max_length=400, help_text="Please enter your first, middle and last name.")
    practice_name = forms.CharField(
        max_length=400, help_text="Please enter the name of your practice")
    email = forms.EmailField(
        max_length=254, help_text="Please enter your email address.")
    phone_number = forms.CharField(
        max_length=30,
        validators=[phone_number_validator], help_text="Please enter your phone number.")
    specialisations = forms.CharField(
        max_length=200, help_text="Please enter your specialisations separated by commas e.g. Cardiology")
    city = forms.CharField(max_length=200, help_text="Please enter your city.")
    address = forms.CharField(
        max_length=200, help_text="Please enter your address (street + number).")
    features = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=OPTIONS,
                                         help_text="Please choose the accessibility options you provide.")

    class Meta:
        model = Doctor
        fields = ('title', 'full_name', 'practice_name', 'email',
                  'phone_number', 'specialisations', 'city', 'address', 'features')

    # Custom validation method to clean up specialisation entries
    def clean_specialisations(self):
        specialisations = self.cleaned_data['specialisations']

        # Split by commas, strip spaces, and remove empty entries
        specialisations_list = [
            spec.strip() for spec in specialisations.split(',') if spec.strip()]

        # If no valid specialisations are provided, raise a validation error
        if not specialisations_list:
            raise ValidationError(
                'Please enter at least one valid specialisation.')

        return specialisations_list


# Create Appointment
class CreateAppointmentForm(forms.ModelForm):

    doctor_specialisation = forms.ModelChoiceField(
        queryset=Specialisation.objects.all(),
        empty_label="Select Specialisation",
        required=True
    )
    doctor_location = forms.ModelChoiceField(
        queryset=Location.objects.all(),
        empty_label="Select Location",
        required=True
    )
    appointment_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        required=True
    )
    additional_info = forms.CharField(widget=forms.Textarea, required=False)

    # Exclude doctor initially, will be populated dynamically via JavaScript dynamic filtering
    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.none(), required=True)

    class Meta:
        model = Appointment
        fields = ['doctor_specialisation', 'doctor_location',
                  'appointment_date', 'additional_info']
        

# Edit Appointment

