"""
URL configuration for care_connect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from doctor_app.views import DoctorListCreateView
from doctor_app.views import DoctorRetreiveUpdateDeleteView

from reservation.views import AppointmentView,AppointmentSummaryView
from reservation.views import AppointmentRetrieveUpdateDeleteView

from accounts.views import AdminCreateView,UserCreateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # admin/user, patient/register

    path('owner/register/', AdminCreateView.as_view()),
    path('patient/register/', UserCreateView.as_view()),

    # doctor 

    path('doctor/', DoctorListCreateView.as_view()),
    path('doctor/<int:pk>/', DoctorRetreiveUpdateDeleteView.as_view()),

    # appointment

    path('appointment/', AppointmentView.as_view()),
    path('appointment/summary/', AppointmentSummaryView.as_view()),
    path('appointment/<int:pk>/', AppointmentRetrieveUpdateDeleteView.as_view()),
    
]
