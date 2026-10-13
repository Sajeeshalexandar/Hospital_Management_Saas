
from django.urls import path
from . import views

urlpatterns = [
    # Keep your existing Super Admin routes too.

    path('', views.doctor_dashboard, name='doctor_dashboard'),
    path('appointments/', views.doctor_appointments,
         name='doctor_appointments'),
    path('patients/', views.doctor_patients,
         name='doctor_patients'),
    path('prescriptions/', views.doctor_prescriptions,
         name='doctor_prescriptions'),
    path('schedule/', views.doctor_schedule,
         name='doctor_schedule'),
    path('profile/', views.doctor_profile,
         name='doctor_profile'),
]
