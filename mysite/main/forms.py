from django import forms

from main.models import Task


class CreateNewTask(forms.Form):
    # title = forms.CharField(label="Title", max_length=100)
    # description = forms.CharField(label="Description", max_length=300)
    # is_done = forms.BooleanField(required=False)

    class Meta:
        # specify model to be used
        model = Task

        # specify fields to be used
        fields = ["title", "description", "is_done", "todolist_id"]


class CreateNewToDoList(forms.Form):
    name = forms.CharField(label="name", max_length=100)
