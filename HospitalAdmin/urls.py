
from django.urls import path
from .import views

urlpatterns = [
    path('',views.Hospital_admin_Dashboard,name='Hospital_admin_Dashboard'),
    path('Doctors/',views.Doctors,name='Doctors'),
    path('Receptionists/',views.Receptionists,name='Receptionists'),
    path('Patients/',views.Patients,name='Patients')
]