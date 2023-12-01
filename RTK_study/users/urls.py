from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('signin/', views.login_user, name='login'),
    path('signout/', views.logout_user, name='logout'),
    path('resetpassword/', views.reset_password, name='resetpassword'),
    path('resetpassword/<int:id>/', views.reset_password, name='resetpassword'),
    path('listusers/', views.listusers, name='listusers'),
    path('removeuser/<int:id>/', views.removeuser, name='removeUser'),
    path('listgroups/', views.listgroups, name='listgroups'),
    path('group/', views.addgroup, name='addgroup'),
    path('group/<int:id>/', views.addgroup, name='addgroup'),
    path('removegroup/<int:id>/', views.removegroup, name='removegroup'),
]
