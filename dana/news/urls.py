# pages/urls.py
from django.contrib import admin
from django.urls import path
from news.views import NewsListView, NewsDetailView

app_name = 'news'

urlpatterns = [
    path('', NewsListView.as_view(), name="news_list"),
    path('index.html', NewsListView.as_view(), name="index"),
    path('news/<int:pk>/', NewsDetailView.as_view(), name="news_detail"),
]
