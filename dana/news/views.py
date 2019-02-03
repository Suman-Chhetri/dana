from django.shortcuts import render
from news.models import News
from django.utils import timezone
from django.views.generic import (View, TemplateView, ListView, FormView, DetailView)

# Create your views here.

class NewsListView(ListView):
    model = News
    tempalte_name = 'news/news_list.html'
    context_object_name = 'all_news_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_page'] = 'active'
        return context

    def get_queryset(self):
        return News.objects.filter(dateAdded__lte=timezone.now()).order_by('-dateAdded')

class NewsDetailView(DetailView):
    model = News
    template_name ='news/news_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_page'] = 'active'
        return context
