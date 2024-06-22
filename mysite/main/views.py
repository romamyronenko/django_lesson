from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from main.forms import CreateNewTask, CreateNewToDoList
from main.models import Task, ToDoList


# Create your views here.
def index(request):
    return render(request, "main/base.html", {})


def todolists(request):
    todolists = ToDoList.objects.all()
    return render(request, "main/todolists.html", {"todolists": todolists})


def todolist(request, id):
    form = CreateNewTask(request.POST or None)
    tasks = Task.objects.filter(todolist=id)

    if form.is_valid():
        t = form.save(commit=False)
        t.todolist = ToDoList.objects.get(id=id)
        t.save()

    return render(
        request, "main/tasks.html", {"tasks": tasks, "form": form, "list_id": id}
    )


def task(request, id):
    task = Task.objects.get(id=id)

    return render(request, "main/task.html", {"task": task})


def create(request):
    form = CreateNewToDoList(request.POST or None)
    if form.is_valid():
        t = form.save(commit=False)
        t.user = request.user
        t.save()

        return redirect(f"main:todolist", t.id)
    return render(request, "main/create_list.html", {"form": form})
