
from django.urls import path
from .import views

urlpatterns = [
    path('',views.SuperAdmin_Dashboard,name='SuperAdmin_Dashboard')
]