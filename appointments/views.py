from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from .models import Appointment


def book_appointment(request):

    if request.method == "POST":

        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        date=request.POST['date']

        Appointment.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message,
            preferred_date=date
        )

        send_mail(
            "New Appointment",
            f"New appointment booked by {name}",
            settings.EMAIL_HOST_USER,
            ["doctor@email.com"],
        )

    return render(request,"appointment.html")