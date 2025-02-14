from django.shortcuts import render
from django.views import generic
from .models import Appointment
from .forms import RoleForm, PatientProfileForm, DoctorProfileForm


# Create your views here.
class AppointmentList(generic.ListView):
    queryset = Appointment.objects.all()
    template_name = "doctor_appointments/index.html"
    paginate_by = 6


def view_appointment(request, appointment_id):
    queryset = Appointment.objects.all()
    appointment = get_object_or_404(queryset, appointment_id=appointment_id)

    return render(
        request,
        "doctor_appointments/view_appointment.html",
        {"appointment": appointment}
    )


def view_role_form(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Your role was saved')

    else:
        form = RoleForm()
        context = {
            'form': form,
        }
    return render(request, 'doctor_appointments/role_choice.html', context)


def view_patient_profile_form(request):
    if request.method == 'POST':
        form = PatientProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Your Profile was set up correctly')

    else:
        form = PatientProfileForm()
        context = {
            'form': form,
        }
    return render(request, 'doctor_appointments/setup_patient_profile.html', context)


def view_doctor_profile_form(request):
    if request.method == 'POST':
        form = DoctorProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Your Profile was set up correctly')

    else:
        form = DoctorProfileForm()
        context = {
            'form': form,
        }
    return render(request, 'doctor_appointments/setup_doctor_profile.html', context)



