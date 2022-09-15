from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from tasks.models import Task

# Create your views here.


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def get_success_url(self):
        return reverse_lazy("show_project", args=[self.object.project.id])


# def form_valid(self, form):
#     form.save()
#     return redirect("list_projects")


class SelfTaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/my_tasks.html"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class TaskCompletionUpdateView(UpdateView):
    model = Task
    template_name = "tasks/update.html"
    fields = ["is_completed"]
    success_url = reverse_lazy("show_my_tasks")
