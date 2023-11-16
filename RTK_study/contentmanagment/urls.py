from django.urls import path
from . import views

urlpatterns = [
    path('addnews/', views.addnews, name='addNews'),
    path('addnews/<int:news_id>/', views.addnews, name='addNews'),
    path('newslist/', views.newschange, name='news-list'),
    path('removenews/<int:news_id>/', views.removenews, name='removeNews'),
]
