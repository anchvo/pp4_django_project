from django.shortcuts import render
from django.views import generic
from .models import Appointment


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


