from django.urls import path
from.import views

urlpatterns=[

    path('',views.Hospadmin_dash,name='HospitalAdmin_Dashboard'),
    path('doctors/', views.doctors_list, name='doctors_list'),
     path("doctors/<str:doctor_id>/",views.doctor_detail,name="doctor_detail"),
     path("doctors/<str:doctor_id>/edit/",views.doctor_edit,name="doctor_edit"),
]