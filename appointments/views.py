from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AppointmentForm
from .models import Appointment
from django.contrib.auth import get_user_model

User = get_user_model()


# ✅ Patient: Book Appointment
@login_required
def book_appointment(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        doctor_id = request.POST.get('doctor')  # Make sure doctor selection is in your form

        if date and time and doctor_id:
            doctor = User.objects.get(id=doctor_id)
            Appointment.objects.create(
                patient=request.user,
                doctor=doctor,
                date=date,
                time=time
            )
            messages.success(request, f"Appointment booked for {date} at {time}")
            return redirect('view_appointments')  # Use correct URL name
        else:
            messages.error(request, "Please fill all fields.")
    return render(request, 'appointments/book.html')

# ✅ Patient: View their own appointments
@login_required
def view_appointments(request):
    if request.user.role == 'PATIENT':
        appointments = Appointment.objects.filter(patient=request.user)
    else:
        appointments = []
        messages.error(request, "Only patients can view this page.")
    return render(request, 'appointments/my_appointments.html', {'appointments': appointments})



@login_required
def manage_appointments(request):
    if request.user.role == 'DOCTOR':
        appointments = Appointment.objects.filter(doctor=request.user)
        form = AppointmentForm()  # instantiate the form if you want to display it
    else:
        appointments = []
        form = None
        messages.error(request, "Only doctors can view this page.")

    return render(request, 'appointments/manage.html', 
                  {'form': form, 'appointments': appointments})


# ✅ Doctor: Set Availability (Placeholder)
@login_required
def set_availability(request):
    return render(request, 'appointments/availability.html')


# ✅ Appointment List (General Page)
@login_required
def appointment_list_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appt = form.save(commit=False)
            appt.patient = request.user
            appt.save()
            messages.success(request, 'Appointment booked successfully.')
            return redirect('appointments')
    else:
        form = AppointmentForm()

    if request.user.role == 'DOCTOR':
        items = Appointment.objects.filter(doctor=request.user).order_by('-date', '-time')
    else:
        items = Appointment.objects.filter(patient=request.user).order_by('-date', '-time')

    return render(request, 'appointments/appointments.html', {'form': form, 'appointments': items})

# ✅ Placeholder for Availability (keep it for now)
@login_required
def availability_placeholder(request):
    return render(request, 'appointments/availability.html')
