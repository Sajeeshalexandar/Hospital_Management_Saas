
from django.shortcuts import render


def doctor_dashboard(request):
    return render(request, 'doctor_panel/dashboard.html')


def doctor_appointments(request):
    return render(request, 'doctor_panel/appointments.html')


def doctor_patients(request):
    return render(request, 'doctor_panel/patients.html')


def doctor_prescriptions(request):
    return render(request, 'doctor_panel/prescriptions.html')


def doctor_schedule(request):
    return render(request, 'doctor_panel/schedule.html')


def doctor_profile(request):
    return render(request, 'doctor_panel/profile.html')
