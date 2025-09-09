from django.urls import path
from . import views

urlpatterns = [
    # Patient URLs
    path('book/', views.book_appointment, name='book_appointment'),   # Book appointment
    path('my/', views.view_appointments, name='view_appointments'),   # Patient's appointments

    # Doctor URLs
    path('manage/', views.manage_appointments, name='manage_appointments'),  # Doctor manages appointments
    path('set-availability/', views.set_availability, name='set_availability'),  # Doctor sets availability

    # Your original ones (optional, if needed for backward compatibility)
    path('', views.appointment_list_create, name='appointments'),
    path('availability/', views.availability_placeholder, name='availability'),
]
