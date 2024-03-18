from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.disk_list, name='disk_list'),
    path('create/', views.disk_create, name='disk_create'),
    path('retrieve/<int:pk>/', views.disk_retrive, name='disk_retrive'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
