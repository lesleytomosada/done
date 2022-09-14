from django.shortcuts import redirect
from django.views.generic.edit import CreateView
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
