from django.contrib.auth.models import User
from django.db import models


class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='todolist')

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_done = models.BooleanField()

    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.id}] {self.title} | {self.description}"
