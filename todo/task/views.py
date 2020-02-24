from django.shortcuts import render, redirect
from .forms import *
from .models import Task


def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')
    context = {'tasks': tasks, 'form': form}
    return render(request, 'task/list.html', context)
