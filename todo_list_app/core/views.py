from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from . models import Task

class Task_List(ListView):
    model = Task
    context_object_name = 'tasks'

class Task_Detail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'core/task.html'

class Task_Create(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks')