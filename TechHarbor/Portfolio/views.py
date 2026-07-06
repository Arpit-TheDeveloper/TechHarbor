from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "portfolio/home.html")


def about(request):
    return render(request, "portfolio/about.html")


def skills(request):
    return render(request, "portfolio/skills.html")


def project(request):
    return render(request, "portfolio/project.html")


def experience(request):
    return render(request, "portfolio/experience.html")


def certification(request):
    return render(request, "portfolio/certification.html")


def contact(request):
    return render(request, "portfolio/contact.html")


# Contact form query
def contact_form(request):
    print("EMAIL_HOST:", settings.EMAIL_HOST)
    print("EMAIL_PORT:", settings.EMAIL_PORT)
    print("EMAIL_HOST_USER:", settings.EMAIL_HOST_USER)
    print("PASSWORD EXISTS:", settings.EMAIL_HOST_PASSWORD is not None)
    
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")
        try:
            subject=f"Hey...!!, this is {name}. Please take my query."
            body=f"""
            Name : {name}
            Email :{email}
            Message : {message}
            
            """
            send_mail(
                subject=subject,
                message=body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False
            )

            messages.success(request, "☑️ Message sent successfully")

        except Exception as e:
            messages.error(request, f"❎ Unable to send message: {e}")

    return redirect("contact")