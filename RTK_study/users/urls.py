from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('signin/', views.login_user, name='login'),
    path('signout/', views.logout_user, name='logout'),
]
