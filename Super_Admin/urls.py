
from django.urls import path
from .import views

urlpatterns = [
    path('',views.SuperAdmin_Dashboard,name='SuperAdmin_Dashboard'),
    path('Hospitals/',views.Hospitals,name='Hospitals'),
    path('Doctors/',views.Doctors,name='Doctors'),
    path('Receptionists/',views.Receptionists,name='Receptionists'),
    path('Patients/',views.Patients,name='Patients')
]