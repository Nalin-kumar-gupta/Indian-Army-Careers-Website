from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
     path('', views.TaskForceListCreateView.as_view()),
     path('send/', views.TaskForceApplicationListCreateView.as_view()),
     
]
