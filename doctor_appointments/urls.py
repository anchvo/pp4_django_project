from . import views
from django.urls import path


urlpatterns = [
    path('', views.view_index, name='home'),
    path('404/', views.view_404page, name='view_404page'),
    path('appointments/', views.view_all_appointments, name='view_all_appointments'),
    path('create_appointment/', views.view_create_appointment,
         name='view_create_appointment'),
    path('delete_appointment/<int:appointment_id>/', views.view_delete_appointment, name='view_delete_appointment'),
    path('edit_appointment/<int:appointment_id>/', views.view_edit_appointment,
         name='view_edit_appointment'),
    path('get-doctors/', views.get_doctors, name='get_doctors'),  # JS Ajax Function in views.py
    path('profile_choice/', views.view_profile_choice, name='view_profile_choice'),
    path('profile_view/', views.view_profile_view, name='view_profile_view'),
    path('setup_doctor_profile/', views.view_doctor_profile_form,
         name='view_doctor_profile_form'),
    path('setup_patient_profile/', views.view_patient_profile_form,
         name='view_patient_profile_form'),
]
