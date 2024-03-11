from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.disk_list, name='disk_list'),
    path('create/', views.disk_create, name='disk_create'),
    path('retrieve/<int:pk>/', views.disk_retrive, name='disk_retrive'),
]
