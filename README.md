# Capstone-Project

# 🏥 Doctor-Patient Appointment Maker

This is a Django-based web application designed to streamline the process of booking medical appointments. Built as a capstone project, it demonstrates full-stack development skills including authentication, database modeling, and dynamic dashboard rendering.

##  Features

- **User Authentication**: Secure login and registration for doctors and patients.
- **Role-Based Access**: Doctors and patients have distinct dashboards and permissions.
- **Appointment Scheduling**: Patients can book, view, and cancel appointments.
- **Doctor Availability**: Doctors can set available time slots and manage bookings.
- **Responsive Design**: Clean UI built with Tailwind CSS for mobile and desktop.
- **Admin Panel**: Django admin interface for managing users and appointments.

## Tech Stack

| Layer        | Technology         |
|--------------|--------------------|
| Frontend     | HTML, Tailwind CSS |
| Backend      | Django             |
| Database     | SQLite (default)   |
| Auth System  | Django Auth Views  |

## Installation

```bash
git clone https://github.com/Bez-coder/Capstone-Project.git
cd Capstone-Project
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
