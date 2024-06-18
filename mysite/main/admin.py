from django.contrib import admin

from main.models import Task, ToDoList

# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Task)
