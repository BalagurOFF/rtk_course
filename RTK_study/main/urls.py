from django.urls import path
from . import views

handler404 = views.handler404

urlpatterns = [
    path('', views.news, name='news'),
    path('news/<int:id>/', views.new_full, name='newsFull'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]
