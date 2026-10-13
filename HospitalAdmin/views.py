from django.shortcuts import render
from django.http import Http404


# Create your views here.
def Hospadmin_dash(request):
    return render(request,'hospitaladmin_dash.html')

def doctors_list(request):
    return render(request, 'doctors_list.html')

def doctor_detail(request, doctor_id):

    doctors = {
        "DOC001": {
            "id": "DOC001",
            "name": "Dr. Arun Kumar",
            "specialization": "Cardiology",
            "department": "Cardiology",
            "contact": "9876543210",
            "status": "Active",
        },
        "DOC002": {
            "id": "DOC002",
            "name": "Dr. Meera Nair",
            "specialization": "Dermatology",
            "department": "Dermatology",
            "contact": "9876543211",
            "status": "Active",
        },
        "DOC003": {
            "id": "DOC003",
            "name": "Dr. Rahul Das",
            "specialization": "Orthopedics",
            "department": "Orthopedics",
            "contact": "9876543212",
            "status": "Inactive",
        },
    }

    doctor = doctors.get(doctor_id)

    if doctor is None:
        raise Http404("Doctor not found")

    return render(
        request,
        "doctor_detail.html",
        {"doctor": doctor}
    )

def doctor_edit(request, doctor_id):
    doctors = {
        "DOC001": {
            "id": "DOC001",
            "name": "Dr. Arun Kumar",
            "specialization": "Cardiology",
            "department": "Cardiology",
            "contact": "9876543210",
            "status": "Active",
        },
        "DOC002": {
            "id": "DOC002",
            "name": "Dr. Meera Nair",
            "specialization": "Dermatology",
            "department": "Dermatology",
            "contact": "9876543211",
            "status": "Active",
        },
        "DOC003": {
            "id": "DOC003",
            "name": "Dr. Rahul Das",
            "specialization": "Orthopedics",
            "department": "Orthopedics",
            "contact": "9876543212",
            "status": "Inactive",
        },
    }

    doctor = doctors.get(doctor_id)

    if doctor is None:
        from django.http import Http404
        raise Http404("Doctor not found")

    return render(request, "doctor_edit.html", {"doctor": doctor})