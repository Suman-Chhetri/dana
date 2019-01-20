from django.shortcuts import render
from django.utils import timezone
from news.models import News
from users.models import CustomUser
from core.models import Intro
from django.views.generic import (View, TemplateView, ListView, FormView, DetailView)

# Create your views here.

class IndexTemplateView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users_list'] = CustomUser.objects.all()
        context['news_list'] = News.objects.all()
        context['intro_view'] = Intro.objects.all().order_by('-id')
        return context

class ContactTemplateView(TemplateView):
    template_name = 'core/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_page'] = 'active'
        context['users_list'] = CustomUser.objects.all()
        context['news_list'] = News.objects.all()
        return context

class AboutView(TemplateView):
    template_name = 'core/aboutus.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_page'] = 'active'
        context['users_list'] = CustomUser.objects.all()
        context['news_list'] = News.objects.all()
        return context
