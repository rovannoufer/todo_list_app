from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
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

class Task_Update(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks')


class Task_Delete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')


class Custom_Login(LoginView):
    template_name = 'core/login.html'
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')