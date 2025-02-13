from . import views
from django.urls import path


urlpatterns = [
    path('', views.AppointmentList.as_view(), name='home'),
]