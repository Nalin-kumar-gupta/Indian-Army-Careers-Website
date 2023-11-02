from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('upload-data/', views.ExcelUploadView.as_view()),
    path('task-force/', views.SortByTaskForceListView.as_view()),
    path('city/', views.SortByCityListView.as_view()),
    path('gender/', views.SortByGenderListView.as_view()),
    path('', views.SortByTaskForceListView.as_view()),
    path('', views.SortByTaskForceListView.as_view()),
    path('', views.SortByTaskForceListView.as_view()),
    path('', views.SortByTaskForceListView.as_view()),
    
]