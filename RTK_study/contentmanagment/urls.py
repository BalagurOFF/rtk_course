from django.urls import path
from . import views

urlpatterns = [
    path('addnews/', views.addnews, name='addNews'),
]
