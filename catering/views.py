from django.shortcuts import render, redirect
from .models import Client, Event, Menu, Order
from .models import Client
from .models import ContactMessage  # Assuming you store messages in DB
from django.core.mail import send_mail
from django.contrib import messages

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        # Save to database
        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)

        # Send email (Optional)
        send_mail(
            subject=f"New Contact Message: {subject}",
            message=f"From: {name} ({email})\n\n{message}",
            from_email="your_email@example.com",
            recipient_list=["admin@example.com"],
            fail_silently=True,
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact")

    return render(request, "contact.html")

def client_list(request):
    clients = Client.objects.all()
    return render(request, "client_list.html", {"clients": clients})

def add_client(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        if name and contact and email:
            Client.objects.create(name=name, contact=contact, email=email)
            return redirect("client_list")  # No extra space!
    return render(request, "add_client.html")

def add_event(request):
    return render(request, 'add_event.html')



def home(request):
    clients = Client.objects.all()  # Fetch all clients
    events = Event.objects.all()  # Fetch all events
    return render(request, 'catering/home.html', {'clients': clients, 'events': events})

