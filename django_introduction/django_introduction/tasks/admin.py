from django.contrib import admin
from django_introduction.tasks.models import Task


@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
    pass
