from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Appointment
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
            form.save()
            return HttpResponse('Your Profile was set up correctly')

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
            form.save()
            return HttpResponse('Your Profile was set up correctly')
        else:
            print(form.errors)  # Check form errors
            # If the form is invalid, render form with errors
            return render(
                request,
                'doctor_appointments/setup_doctor_profile.html',
                {
                    'form': form,  # Show the form with error messages
                    'error_message': 'Please correct the errors below.' # Optional error message
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
