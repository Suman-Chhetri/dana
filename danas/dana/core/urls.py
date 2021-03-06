# core/urls.py
from django.contrib import admin
from django.urls import path
from core.views import IndexTemplateView, ContactTemplateView, AboutView, MembersView, CMembersView, GalleryView

app_name = 'core'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name="index"),
    path('contact', ContactTemplateView.as_view(), name="contact"),
    path('contact.html', ContactTemplateView.as_view(), name="contacth"),
    path('about', AboutView.as_view(), name="about"),
    path('about.html', AboutView.as_view(), name="abouth"),
    path('members', MembersView.as_view(), name="members"),
    path('cmembers', CMembersView.as_view(), name="cmembers"),
    path('members.html', MembersView.as_view(), name="membersh"),
    path('gallery', GalleryView.as_view(), name="gallery"),
]
