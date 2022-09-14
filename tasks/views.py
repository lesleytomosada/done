from asyncio import tasks
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from tasks.models import Task
from projects.models import Project


# Create your views here.
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def form_valid(self, form):
        form.save()
        return redirect("list_projects")


class SelfTaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/my_tasks.html"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)
