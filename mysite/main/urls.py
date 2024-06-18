from django.urls import path

from main import views

urlpatterns = [
    path("", views.index),
    path("tasks/", views.tasks),
    path("task/<int:id>", views.task),
    path("create/", views.create),
]
