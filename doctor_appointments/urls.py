from . import views
from django.urls import path


urlpatterns = [
    path('', views.AppointmentList.as_view(), name='home'),
    path('<int:appointment_id>/', views.view_appointment, name='view_appointment'),
    path('role_choice/', views.view_role_form, name='view_role_form')
]
