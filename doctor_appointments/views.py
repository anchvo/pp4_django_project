from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import PatientProfileForm, DoctorProfileForm, CreateAppointmentForm
from .models import Appointment, Patient, Doctor, Location, Specialisation


# Create your views here.


# Index / Home Page
def view_index(request):

    return render(request, 'doctor_appointments/index.html')


# Profile Choice Page
def view_profile_choice(request):

    return render(request, 'doctor_appointments/profile_choice.html')


# Setup Patient Profile Form & Page
def view_patient_profile_form(request):
    # Check if the user already has a patient profile
    if hasattr(request.user, 'patient'):
        # If the user already has a patient profile, redirect to the profile view
        messages.info(request, "You already have a patient profile.")
        return redirect('view_profile_view')

    if request.method == 'POST':
        form = PatientProfileForm(data=request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user  # Assign the logged-in user to the Patient instance
            patient.save()

            messages.success(
                request, "Your patient profile has been created successfully!")
            # Redirects to User Profile View
            return redirect('view_profile_view')

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


# Setup Doctor Profile Form & Page
def view_doctor_profile_form(request):

    # Create empty Doctor instance / variable
    doctor = None

    if request.method == 'POST':
        form = DoctorProfileForm(data=request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.user = request.user  # Assign the logged in user to the Doctor instance

            # Save Doctor Instance
            doctor.save()

            # Save the selected features (checkboxes) as a joined string
            # Join selected values as comma-separated string
            selected_features = ','.join(form.cleaned_data['features'])
            doctor.features = selected_features

            # Save Doctor instance with features
            doctor.save()

            # Save user input location to Location model
            # Check if location already exists / retrieve object
            location = Location.objects.filter(doctors=doctor).first()
            if not location:
                city_name = form.cleaned_data['city']
                location, created = Location.objects.get_or_create(city=city_name)
                doctor.locations.add(location)

            # Save specialisations as a comma-separated string in the Doctor model
            specialisation_names = form.cleaned_data['specialisations']
            specialisation_objs = []

            for spec in specialisation_names:
                spec = spec.strip()
                if spec:
                    obj, created = Specialisation.objects.get_or_create(specialisation_name=spec)
                    specialisation_objs.append(obj)

            doctor.specialisations.set(specialisation_objs)

            # Redirects to User Profile View
            return redirect('view_profile_view')

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

    else:  # If the request method is GET, refer back to form
        form = DoctorProfileForm()

    return render(
        request,
        'doctor_appointments/setup_doctor_profile.html',
        {
            'form': form
        },
    )


# Profile View Page, depending on logged in status as Doctor or Patient
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
        appointments = Appointment.objects.filter(doctor=doctor_profile).filter(
            appointment_date__gte=timezone.now()).order_by('appointment_date')
    elif patient_profile:
        appointments = Appointment.objects.filter(patient=patient_profile).filter(
            appointment_date__gte=timezone.now()).order_by('appointment_date')

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


# Create Appointment Form & Page
@login_required  # Page only visible to logged in users
def view_create_appointment(request):

    if request.method == 'POST':

        specialisation_id = request.POST.get('doctor_specialisation')
        location_id = request.POST.get('doctor_location')

        form = CreateAppointmentForm(request.POST)

        if specialisation_id and location_id:
            try:
                specialisation = Specialisation.objects.get(id=specialisation_id)
                doctors = Doctor.objects.filter(
                    locations__id=location_id,
                    specialisations=specialisation
                ).distinct()
                form.fields['doctor'].queryset = doctors
            except Specialisation.DoesNotExist:
                form.fields['doctor'].queryset = Doctor.objects.none()

        if form.is_valid():

            # Ensure a valid doctor is chosen
            doctor = form.cleaned_data.get('doctor')
            if not doctor:
                form.add_error('doctor', 'You must select a valid doctor.')
                return render(request, 'doctor_appointments/create_appointment.html', {'form': form})

            # Save new appointment with the current user
            appointment = form.save(commit=False)
            appointment.patient = Patient.objects.get(user=request.user)

            # Ensure the doctor is set
            doctor = form.cleaned_data.get('doctor')
            if doctor:
                appointment.doctor = doctor
            else:
                form.add_error('doctor', 'You must select a doctor.')

            appointment.save()
            # Redirect to the profile view after successful creation
            return redirect('view_all_appointments')
    else:
        # Ddoctors are filtered based on the selected specialisation and location
        specialisation_id = request.GET.get('specialisation', None)
        location_id = request.GET.get('location', None)

        # Initialize the form
        form = CreateAppointmentForm()

        # If specialisation and location are provided in the GET parameters, filter the doctors
        if specialisation_id and location_id:
            doctors = Doctor.objects.filter(
                # Use contains for flexible matching
                specialisations__specialisation_name__icontains=specialisation_id,
                locations__city__icontains=location_id  # Use city to filter location
            )
            # Update the form's doctor queryset based on the filter
            form.fields['doctor'].queryset = doctors

    return render(request, 'doctor_appointments/create_appointment.html', {'form': form})


# Handle Ajax request for Doctor JS dynamic filtering without reloading page
# JavaScript function triggers this view
def get_doctors(request):
    specialisation_id = request.GET.get('specialisation')
    location_id = request.GET.get('location')

    # If specialisation or location are not selected, return an empty list
    if not specialisation_id or not location_id:
        return JsonResponse({'doctors': []})

    # Fetch the name of the specialisation based on the id passed in the GET request
    try:
        specialisation = Specialisation.objects.get(id=specialisation_id)
    except Specialisation.DoesNotExist:
        # Return empty if the specialisation doesn't exist
        return JsonResponse({'doctors': []})

    # Filter doctors by matching specialisation and location
    doctors = Doctor.objects.filter(
        locations__id=location_id,
        specialisations=specialisation
    ).distinct()

    # Create a list of doctors to return in the JSON response
    doctor_data = [{'id': doctor.id, 'full_name': doctor.full_name}
                   for doctor in doctors]

    return JsonResponse({'doctors': doctor_data})


# Appointment List on Appointments Page
@login_required  # Page only visible to logged in users
def view_all_appointments(request):
    # Initialize variables for the profiles and appointments
    doctor_profile = None
    patient_profile = None
    # Start with an empty queryset to avoid NoneType errors
    appointments = Appointment.objects.none()

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
        appointments = Appointment.objects.filter(
            doctor=doctor_profile).order_by('appointment_date')
    elif patient_profile:
        appointments = Appointment.objects.filter(
            patient=patient_profile).order_by('appointment_date')

    # Paginate the appointments
    paginator = Paginator(appointments, 6)  # Show 6 appointments per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'doctor_profile': doctor_profile,
        'patient_profile': patient_profile,
        'appointments': page_obj,
    }

    return render(request, 'doctor_appointments/appointments.html', context)


# Edit Appointment
@login_required
def view_edit_appointment(request, appointment_id):
    # Fetch the appointment object that needs to be edited
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method == 'POST':
        # Bind the form with the existing appointment data
        form = CreateAppointmentForm(request.POST, instance=appointment)

        # Set the fields as non-required when submitting (to avoid validation errors)
        form.fields['doctor_specialisation'].required = False
        form.fields['doctor_location'].required = False
        form.fields['doctor'].required = False

        if form.is_valid():
            # Save the updated appointment
            form.save()
            # Redirect to profile view
            return redirect('view_all_appointments')
    else:
        # For GET request, pass the existing appointment data to the form
        form = CreateAppointmentForm(instance=appointment)

        # Make the fields readonly (non-editable)
        form.fields['doctor_specialisation'].widget.attrs['readonly'] = True
        form.fields['doctor_location'].widget.attrs['readonly'] = True
        form.fields['doctor'].widget.attrs['readonly'] = True

        # Set the fields as non-required dynamically for this form
        form.fields['doctor_specialisation'].required = False
        form.fields['doctor_location'].required = False
        form.fields['doctor'].required = False

        # Use disabled to prevent form submission from including the fields' values
        form.fields['doctor_specialisation'].widget.attrs['disabled'] = 'disabled'
        form.fields['doctor_location'].widget.attrs['disabled'] = 'disabled'
        form.fields['doctor'].widget.attrs['disabled'] = 'disabled'

        # Ensure initial values for doctor_specialisation, doctor_location, and doctor
        form.fields['doctor_specialisation'].initial = appointment.doctor_specialisation
        form.fields['doctor_location'].initial = appointment.doctor_location
        form.fields['doctor'].initial = appointment.doctor

    return render(request, 'doctor_appointments/edit_appointment.html', {'form': form})


# Delete Appointment
@login_required
def view_delete_appointment(request, appointment_id):
    # Fetch the appointment object using the appointment_id from the URL
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method == 'POST':
        # Proceed with the deletion if it's a POST request
        appointment.delete()
        messages.success(request, 'Appointment successfully deleted.')
        # Redirect to the appointment management page
        return redirect('view_all_appointments')

    # If it's a GET request, show a confirmation message or page

    # Redirect to appointments list by default
    return redirect('view_all_appointments')


# 404 Error Page
def view_404page(request):

    return render(request, 'doctor_appointments/404.html')
