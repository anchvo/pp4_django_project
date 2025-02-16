from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views import generic
from .forms import PatientProfileForm, DoctorProfileForm, CreateAppointmentForm
from .models import Appointment, Patient, Doctor, Location, Specialisation



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
    
    # Check if Doctor instance already exists to avoid database errors with OneToOne unique User to Doctor relationship
    try:
        doctor = Doctor.objects.get(user=request.user)
        is_update = True  # Track if it's an update to existing profile
    except Doctor.DoesNotExist:
        doctor = None
        is_update = False
    
    if request.method == 'POST':
        form = DoctorProfileForm(data=request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.user = request.user  # Assign the logged-in user to the Doctor instance
            doctor.save()

            # Save the selected features (checkboxes) as a joined string
            selected_features = ','.join(form.cleaned_data['features'])  # Join selected values as comma-separated string
            doctor.features = selected_features
            doctor.save()

            # Save user input location to Location model 
            location = Location(doctor=doctor, city=form.cleaned_data['city'])
            location.save()

            # Save user input specialisations to Specialisation model
            specialisations = form.cleaned_data['specialisations'].split(',')  # Splitting by comma-separated list
            for spec in specialisations:
                spec = spec.strip()  # Clean extra spaces
                specialisation = Specialisation(doctor=doctor, specialisations=spec)
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

    else:  # If the request method is GET, display the form (pre-filled if it's an update)
        form = DoctorProfileForm(instance=doctor)

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
    next_appointment = None

    # Ensure logged in users can only access their own profile

    # Check for Doctor or Patient profile
    try:
        doctor_profile = Doctor.objects.get(user=request.user)
        patient_profile = None  # Ensure patient_profile is None if it's a doctor
    except Doctor.DoesNotExist:
        doctor_profile = None
        try:
            patient_profile = Patient.objects.get(user=request.user)
        except Patient.DoesNotExist:
            patient_profile = None

    # Fetch Appointments & filter for next date / Ensure they only see their own profile data
    appointments = []
    if doctor_profile:
        appointments = Appointment.objects.filter(doctor=doctor_profile).filter(appointment_date__gte=timezone.now()).order_by('appointment_date')
    elif patient_profile:
        appointments = Appointment.objects.filter(patient=patient_profile).filter(appointment_date__gte=timezone.now()).order_by('appointment_date')

    # Get the next upcoming appointment (if exists)
    next_appointment = appointments.first() if appointments else None

    # Pass context data

    context = {
        'doctor_profile': doctor_profile,
        'patient_profile': patient_profile,
        'next_appointment': next_appointment,
        'appointments': appointments,
    }

    return render(request, 'doctor_appointments/profile_view.html', context)


# Render Create Appointment Form & Page
@login_required
def view_create_appointment(request):
    if request.method == 'POST':
        form = CreateAppointmentForm(request.POST)
        if form.is_valid():
            # Save new appointment with current patient
            appointment = form.save(commit=False)
            patient = Patient.objects.get(user=request.user)
            appointment.patient = patient  # Set patient as logged in user
            appointment.save()
            return redirect('profile_view')  # Redirect to the profile view after successful creation
    else:
        form = CreateAppointmentForm()

    return render(request, 'doctor_appointments/create_appointment.html', {'form': form})


# Handle Ajax request for Doctor JS dynamic filtering via JsonResponse
def get_doctors(request):
    specialisation_id = request.GET.get('specialisation')
    location_id = request.GET.get('location')

    # Filter doctors by specialisation and location
    doctors = Doctor.objects.filter(
        specialisation__id=specialisation_id,
        location__id=location_id
    )

    # Create a list of doctors to return in the JSON response
    doctor_data = [{'id': doctor.id, 'full_name': doctor.full_name} for doctor in doctors]

    return JsonResponse({'doctors': doctor_data})

# Render Appointment List on Appointments Page
@login_required
def view_all_appointments(request):
    # Initialize variables for the profiles and appointments
    doctor_profile = None
    patient_profile = None
    appointments = None

    # Ensure logged in users can only access their own profile

    # Check for Doctor or Patient profile
    try:
        doctor_profile = Doctor.objects.get(user=request.user)
        patient_profile = None  # Ensure patient_profile is None if it's a doctor
    except Doctor.DoesNotExist:
        doctor_profile = None
        try:
            patient_profile = Patient.objects.get(user=request.user)
        except Patient.DoesNotExist:
            patient_profile = None

    # Fetch the appointments / Ensure they only see their own profile data
    if doctor_profile:
        appointments = Appointment.objects.filter(doctor=doctor_profile).order_by('appointment_date')
    elif patient_profile:
        appointments = Appointment.objects.filter(patient=patient_profile).order_by('appointment_date')

    # Paginate the appointments
    paginator = Paginator(appointments, 6)  # Show 6 appointments per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'appointments': page_obj,
    }

    return render(request, 'doctor_appointments/all_appointments.html', context)


# CURRENTLY STORED CODE RELATING TO URLS AND HTIML !! DELETE ALL IF UNUSED !!
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
