from django.http import HttpResponse
from django.shortcuts import render

from main.models import Task


# Create your views here.
def index(request):
    return render(request, "main/base.html", {})


def tasks(request):
    tasks = Task.objects.all()
    return render(request, "main/tasks.html", {"tasks": tasks})


def task(request, id):
    task = Task.objects.get(id=id)

    return render(request, "main/task.html", {"task": task})
