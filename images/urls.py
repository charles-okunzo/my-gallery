from django import views
from django.urls import path, re_path
from . import views



urlpatterns = [
  path('', views.home, name= 'home')
]