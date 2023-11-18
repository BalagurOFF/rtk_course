from django.urls import path
from . import views

urlpatterns = [
    path('addnews/', views.addnews, name='addNews'),
    path('addnews/<int:news_id>/', views.addnews, name='addNews'),
    path('newslist/', views.newschange, name='news-list'),
    path('removenews/<int:news_id>/', views.removenews, name='removeNews'),
    path('regions/', views.regions, name='regions'),
    path('regions/<int:id>/', views.regions, name='regions'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:id>/', views.topics, name='topics'),
]
