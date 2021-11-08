from django.urls import path

from tarefas import views

urlpatterns = [
    path('', views.index),
    path('listar', views.listar)
]