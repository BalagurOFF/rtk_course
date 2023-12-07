from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('news/<int:id>/', views.new_full, name='newsFull'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('contact_messages/', views.ContactMessages.as_view(), name='messages'),
    path('contact_message/<int:pk>/', views.ContactMessageDetail.as_view(), name='messagedetail'),
    path('moderation/', views.moderation, name='moderation'),
]
