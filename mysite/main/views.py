from django.http import HttpResponseRedirect
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


def create(request):
    data = {}
    if request.method == "POST":
        data = dict(request.POST)
        task = Task.objects.create(
            title=data.get('title', [None])[0],
            description=data.get('description', [None])[0],
            is_done=data.get('is_done', [None])[0] == 'on',
        )
        task.save()
        return HttpResponseRedirect(f"/task/{task.id}")
    return render(request, "main/create.html", {'data': data})
