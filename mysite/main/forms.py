from django import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    description = forms.CharField(label="Description", max_length=300)
    is_done = forms.BooleanField(required=False)


class CreateNewToDoList(forms.Form):
    name = forms.CharField(label="name", max_length=100)
