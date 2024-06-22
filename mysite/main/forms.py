from django import forms

from main.models import Task, ToDoList


class CreateNewTask(forms.ModelForm):
    class Meta:
        # specify model to be used
        model = Task

        # specify fields to be used
        fields = ["title", "description", "is_done"]


class CreateNewToDoList(forms.ModelForm):
    class Meta:
        # specify model to be used
        model = ToDoList

        # specify fields to be used
        fields = ["name"]
