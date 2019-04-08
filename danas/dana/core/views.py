from django.shortcuts import render
from django.utils import timezone
from news.models import News
from users.models import Member
from core.models import Intro, Aim, Service, GalleryImage
from django.views.generic import (View, TemplateView, ListView, FormView, DetailView)

# Create your views here.

class IndexTemplateView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_page'] = 'active'
        context['users_list'] = Member.objects.all().order_by('rank', 'username')
        context['news_list'] = News.objects.all()
        context['aims_view'] = Aim.objects.all().order_by('-id')
        context['services_view'] = Service.objects.all().order_by('-id')
        context['intro_view'] = Intro.objects.all().order_by('-id')
        return context

class ContactTemplateView(TemplateView):
    template_name = 'core/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_page'] = 'active'
        context['users_list'] = Member.objects.all().order_by('rank', 'username')
        context['news_list'] = News.objects.all()
        return context

class AboutView(TemplateView):
    template_name = 'core/aboutus.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_page'] = 'active'
        context['users_list'] = Member.objects.all().order_by('rank', 'username')
        context['news_list'] = News.objects.all()
        context['intro_view'] = Intro.objects.all().order_by('-id')
        context['aims_view'] = Aim.objects.all().order_by('-id')
        context['services_view'] = Service.objects.all().order_by('-id')
        return context

class MembersView(TemplateView):
    template_name ='core/members.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members_page'] = 'active'
        context['users_list'] = Member.objects.all().order_by('rank', 'username')
        context['news_list'] = News.objects.all()
        context['aims_view'] = Aim.objects.all().order_by('-id')
        context['services_view'] = Service.objects.all().order_by('-id')
        context['intro_view'] = Intro.objects.all().order_by('-id')
        return context

class CMembersView(TemplateView):
    template_name ='core/cmembers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members2_page'] = 'active'
        context['users_list'] = Member.objects.all().order_by('rank', 'username')
        context['news_list'] = News.objects.all()
        context['aims_view'] = Aim.objects.all().order_by('-id')
        context['services_view'] = Service.objects.all().order_by('-id')
        context['intro_view'] = Intro.objects.all().order_by('-id')
        return context

class GalleryView(TemplateView):
    template_name ='core/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_page'] = 'active'
        context['users_list'] = Member.objects.all().order_by('rank', 'username')
        context['image_list'] = GalleryImage.objects.all().order_by('level')
        context['news_list'] = News.objects.all()
        return context