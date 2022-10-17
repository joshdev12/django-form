from asyncio import tasks
from multiprocessing import context
from django.shortcuts import render
from .forms import TaskForm
from .models import Task
# Create your views here.

def home(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TaskForm()
    tasks = Task.objects.all().order_by('-created')
    context = {
        "tasks": tasks,
        "form": form
        }
    return render(request, "todoapp/home.html", context)

def detail(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
    else:
        form = TaskForm()
    context = {
        "tasks": task,
        "form": form
        }
    return render(request, "todoapp/detail.html", context)

