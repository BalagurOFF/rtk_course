from django.urls import path
from . import views

urlpatterns = [
    path('addnews/', views.addnews, name='addNews'),
    path('addnews/<int:news_id>/', views.addnews, name='addNews'),
    path('newslist/', views.newschange, name='news-list'),
    path('removenews/<int:news_id>/', views.removenews, name='removeNews'),
    path('tags/', views.tags, name='tags'),
    path('tags/<int:id>/', views.tags, name='tags'),
    path('removetag/<int:id>/', views.removetag, name='removetag'),
    path('moderation/', views.moderation, name='moderation'),
    path('adminnewslist/', views.administratenews, name='admin-newslist'),
]
