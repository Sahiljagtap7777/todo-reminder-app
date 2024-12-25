"""
URL configuration for todolist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mytodoapp import views
urlpatterns = [
    
    path('',views.mytodoapp, name='mytodoapp'),
    path('task/',views.task,name='task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('update/<int:id>/', views.update_task, name='update_task'),
    path('delete_all/', views.delete_all_tasks, name='delete_all_tasks'),
]
