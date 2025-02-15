from . import views
from django.urls import path


urlpatterns = [
    path('', views.view_index, name='home'),
    path('appointments/', views.AppointmentList.as_view(), name='appointments'),
    path('create_appointment/', views.view_create_appointment,
         name='view_create_appointment'),
    path('<int:appointment_id>/', views.view_appointment, name='view_appointment'),
    path('profile_choice/', views.view_profile_choice, name='view_profile_choice'),
    path('profile_view/', views.view_profile_view, name='view_profile_view'),
    path('setup_doctor_profile/', views.view_doctor_profile_form,
         name='view_doctor_profile_form'),
    path('setup_patient_profile/', views.view_patient_profile_form,
         name='view_patient_profile_form'),
]
