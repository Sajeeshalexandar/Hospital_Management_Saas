from django.shortcuts import render

# Create your views here.

def Hospital_admin_Dashboard(request):
    return render(request,'Hospital_admin_panel/dashboard.html')
def Receptionists(request):
    return render(request,'Hospital_admin_panel/receptionists.html')
def Doctors(request):
    return render(request,'Hospital_admin_panel/doctors.html')
def Patients(request):
    return render(request,'Hospital_admin_panel/patients.html')
def hospital_profile(request):
    return render(request,'Hospital_admin_panel/hospital_profile.html')
def edit_hospital_profile(request):
    return render(request,'Hospital_admin_panel/edit_hospital_profile.html')