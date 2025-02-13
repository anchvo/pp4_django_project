from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Patient, Doctor, Appointment


@admin.register(Appointment)
class AppointmentAdmin(SummernoteModelAdmin):

    list_display = ('patient', 'doctor', 'appointment_date', 'created_on')
    search_fields = ['patient']
    list_filter = ('doctor', 'appointment_date', 'patient',)
    summernote_fields = ('additional_info',)


# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
