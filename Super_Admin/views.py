from django.shortcuts import render

# Create your views here.

def SuperAdmin_Dashboard(request):
    return render(request,'super_admin_panel/dashboard.html')
def Receptionists(request):
    return render(request,'super_admin_panel/receptionists.html')
def Hospitals(request):
    return render(request,'super_admin_panel/hospitals.html')
def Doctors(request):
    return render(request,'super_admin_panel/doctors.html')
def Patients(request):
    return render(request,'super_admin_panel/patients.html')