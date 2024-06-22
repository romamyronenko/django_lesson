from django.urls import path

from main import views

app_name = "main"
urlpatterns = [
    path("", views.index, name='home'),
    path("todolists/", views.todolists, name='todolists'),
    path("todolist/<int:id>", views.todolist, name='todolist'),
    path("task/<int:id>", views.task, name='task'),
    path("create/", views.create, name='create'),
]
