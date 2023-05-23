from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('taskForm/', views.taskForm, name='taskForm'),
    path('taskUpdate/<str:pk>/', views.taskUpdate, name='taskUpdate'),
    path('taskDelete/<str:pk>/', views.taskDelete, name='taskDelete'),
]
