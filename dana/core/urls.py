# core/urls.py
from django.contrib import admin
from django.urls import path
from core.views import IndexTemplateView, ContactTemplateView, AboutView

app_name = 'core'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name="index"),
    path('contact', ContactTemplateView.as_view(), name="contact"),
    path('contact.html', ContactTemplateView.as_view(), name="contacth"),
    path('about', AboutView.as_view(), name="about"),
    path('about.html', AboutView.as_view(), name="abouth"),
]
