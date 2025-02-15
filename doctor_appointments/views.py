from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Appointment, Patient, Doctor, Location, Specialisation
from .forms import PatientProfileForm, DoctorProfileForm


# Create your views here.

# Render Index / Home Page
def view_index(request):

    return render(request, 'doctor_appointments/index.html')


# Render Profile Choice Page
def view_profile_choice(request):

    return render(request, 'doctor_appointments/profile_choice.html')


# Render Setup Patient Profile Form & Page
def view_patient_profile_form(request):
    if request.method == 'POST':
        form = PatientProfileForm(data=request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user  # Assign the logged-in user to the Patient instance
            patient.save()

            return redirect('view_profile_view')  # Redirects to User Profile View
        
        else:
            # If the form is invalid, render form with errors
            return render(
                request,
                'doctor_appointments/setup_patient_profile.html',
                {
                    'form': form,  # Show the form with error messages
                    'error_message': 'Please correct the errors below.'  # Optional error message
                }
            )

    else:  # If the request method is GET, just display an empty form
        form = PatientProfileForm()

    return render(
        request,
        'doctor_appointments/setup_patient_profile.html',
        {
            'form': form
        },
    )


# Render Setup Doctor Profile Form & Page
def view_doctor_profile_form(request):
    if request.method == 'POST':
        form = DoctorProfileForm(data=request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.user = request.user  # Assign the logged-in user to the Doctor instance
            doctor.save()

            # Save the selected features as a joined string 
            selected_features = ','.join(form.cleaned_data['features'])  # Join selected values as comma-separated string
            doctor.features = selected_features
            doctor.save()

            # Save user input location to Location model 
            location = Location(location=doctor, city=form.cleaned_data['city'])
            location.save()

            # Save user input specialisations to Specialisation model
            specialisations = form.cleaned_data['specialisations'].split(',')  # Splitting by comma-separated list
            for spec in specialisations:
                spec = spec.strip()  # Clean extra spaces
                specialisation = Specialisation(specialisation=doctor, specialisations=spec)
                specialisation.save()

            return redirect('view_profile_view')  # Redirects to User Profile View
        
        else:
            print(form.errors)  # Check form errors
            # If the form is invalid, render form with errors
            return render(
                request,
                'doctor_appointments/setup_doctor_profile.html',
                {
                    'form': form,  # Show the form with error messages
                    'error_message': 'Please correct the errors below.'  # Optional error message
                }
            )

    else:  # If the request method is GET, just display an empty form
        form = DoctorProfileForm()

    return render(
        request,
        'doctor_appointments/setup_doctor_profile.html',
        {
            'form': form
        },
    )


# Render Profile View Page, depending on logged in status as Doctor or Patient
@login_required  # Page only visible to logged in users
def view_profile_view(request):

    # Initialize variables for the profiles and appointments
    doctor_profile = None
    patient_profile = None
    appointments = None

    # Check if logged in user is a Doctor
    try:
        doctor_profile = Doctor.objects.get(user=request.user)
    except Doctor.DoesNotExist:
        doctor_profile = None

    # Check if logged in user is a Patient
    try:
        patient_profile = Patient.objects.get(user=request.user)
    except Patient.DoesNotExist:
        patient_profile = None

    # If logged in user is a Doctor, fetch their appointments
    if doctor_profile:
        appointments = Appointment.objects.filter(doctor=doctor_profile)

    # If logged in user is a Patient, fetch their appointments
    if patient_profile:
        appointments = Appointment.objects.filter(patient=patient_profile)

    context = {
        'doctor_profile': doctor_profile,
        'patient_profile': patient_profile,
        'appointments': appointments,
    }


    return render(request, 'doctor_appointments/profile_view.html', context)


# Render Appointment List on Appointments Page
class AppointmentList(generic.ListView):
    queryset = Appointment.objects.all().order_by('-appointment_date')
    template_name = "doctor_appointments/appointments.html"
    paginate_by = 6


def view_appointment(request, appointment_id):
    queryset = Appointment.objects.all()
    appointment = get_object_or_404(queryset, appointment_id=appointment_id)

    return render(
        request,
        "doctor_appointments/view_appointment.html",
        {"appointment": appointment}
    )
