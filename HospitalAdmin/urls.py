
from django.urls import path
from .import views

urlpatterns = [
    path('',views.Hospital_admin_Dashboard,name='hospital_admin_Dashboard'),
    path('Doctors/',views.Doctors,name='hospital_doctors'),
    path('Receptionists/',views.Receptionists,name='hospital_receptionists'),
    path('Patients/',views.Patients,name='hospital_patients'),
    path('hospital_profile/',views.hospital_profile,name='hospital_profile'),
    path('edit_hospital_profile/',views.edit_hospital_profile,name='edit_hospital_profile'),
]