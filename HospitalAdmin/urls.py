
from django.urls import path
from .import views

urlpatterns = [
    path('',views.Hospital_admin_Dashboard,name='hospital_admin_Dashboard'),
    path('Doctors/',views.Doctors,name='hospital_doctors'),
    path('Receptionists/',views.Receptionists,name='hospital_receptionists'),
    path('Patients/',views.Patients,name='hospital_patients')
]