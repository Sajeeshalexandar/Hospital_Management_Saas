from django.shortcuts import render

# Create your views here.

def SuperAdmin_Dashboard(request):
    return render(request,'SuperAdmin_Dashboard.html')
def Receptionists(request):
    return render(request,'receptionists.html')
def Hospitals(request):
    return render(request,'hospitals.html')
def Doctors(request):
    return render(request,'doctors.html')
def Patients(request):
    return render(request,'patients.html')