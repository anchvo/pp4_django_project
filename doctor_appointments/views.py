from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Appointment
from .forms import RoleForm, PatientProfileForm, DoctorProfileForm


# Create your views here.
def view_index(request):

    return render(request, 'doctor_appointments/index.html')


class AppointmentList(generic.ListView):
    queryset = Appointment.objects.all()
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


def view_doctor_profile_form(request):
    if request.method == 'POST':
        form = DoctorProfileForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Your Profile was set up correctly')

    form = DoctorProfileForm()

    return render(
        request,
        'doctor_appointments/setup_doctor_profile.html',
        {
            'form': form
        },
    )


def view_profile_choice(request):

    return render(request, 'doctor_appointments/profile_choice.html')
