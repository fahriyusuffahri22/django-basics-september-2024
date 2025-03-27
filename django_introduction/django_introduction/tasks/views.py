from django.shortcuts import render
from django_introduction.tasks.models import Task


def index(request):
    tasks_list = Task.objects.all()
    context = {
        'tasks_list': tasks_list
    }
    return render(request, 'tasks/index.html', context)
