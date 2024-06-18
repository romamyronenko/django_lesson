from django.urls import path

from main import views

urlpatterns = [
    path("", views.index),
    path("todolists/", views.todolists),
    path("todolist/<int:id>", views.todolist),
    path("task/<int:id>", views.task),
    path("create/", views.create),
]
