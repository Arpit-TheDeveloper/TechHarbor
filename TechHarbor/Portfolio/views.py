from django.shortcuts import render

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


def hireme(request):
    return render(request, "portfolio/hireme.html")