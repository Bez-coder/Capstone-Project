
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created and logged in.')
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    description = """MediMeet is a simple appointment booking system built as a capstone project.
It lets patients book appointments and doctors view their booked appointments. Use the navigation to access features."""
    return render(request, 'accounts/dashboard.html', {'description': description})
