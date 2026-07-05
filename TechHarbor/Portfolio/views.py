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


def query(request):
    try:
        if request.method=="POST":
            name=request.POST.get("name")
            email=request.POST.get("email")
            message=request.POST.get("message")

            
    except:
        pass
    return render(request, "portfolio/contact.html")