from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("skills/", views.skills, name="skills"),
    path("project/", views.project, name="project"),
    path("experience/", views.experience, name="experience"),
    path("certification/", views.certification, name="certification"),
    path("contact/", views.contact, name="contact"),

    path("contact/submit/", views.contact_form, name="contact_form")
]