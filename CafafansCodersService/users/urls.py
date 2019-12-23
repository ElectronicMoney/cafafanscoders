"""
CafafansCodersService URL Configuration
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users_index'),
]
