from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from .forms import TaskUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin


from django.views import View

from .models import Task


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todoapp/task_list.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskUpdateForm
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    success_url = reverse_lazy("task_list")
    form_class = TaskUpdateForm
    template_name = "todoapp/update_task.html"
    context_object_name = "task"

    def post(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.complete = False
        object.save()
        return super().post(request, *args, **kwargs)


class TaskComplete(LoginRequiredMixin, View):
    # model = Task
    successurl = reverse_lazy("task_list")

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.complete = True
        object.save()
        return redirect(self.successurl)


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("task_list")
