from django.http import HttpResponseRedirect
from django.shortcuts import render

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

    if request.method == "POST":

        data = {}
        for key in ["title", "description", "is_done", "todolist_id"]:
            data[key] = request.POST.get(key)

        data["is_done"] = bool(data["is_done"] == "on")
        task = Task(**data)
        print(request.POST["title"])
        task.save()
        return render(
            request, "main/tasks.html", {"tasks": tasks, "form": form, "list_id": id}
        )
    return render(
        request, "main/tasks.html", {"tasks": tasks, "form": form, "list_id": id}
    )


def task(request, id):
    task = Task.objects.get(id=id)

    return render(request, "main/task.html", {"task": task})


def create(request):
    data = {}
    if request.method == "POST":
        data = dict(request.POST)
        todolist = ToDoList.objects.create(
            name=data.get("name", [None])[0],
        )
        todolist.save()
        return HttpResponseRedirect(f"/todolist/{todolist.id}")
    form = CreateNewToDoList()
    return render(request, "main/create_list.html", {"data": data, "form": form})
