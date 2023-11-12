from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('news/<int:id_new>/', views.new_full, name='newsFull'),
    path('addnews/', views.addnews, name='addNews'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),

]
