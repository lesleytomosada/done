from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect

from projects.models import Project

# Create your views here.


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/list.html"

    def get_query(self):
        return Project.objects.filter(members=self.request.user)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/detail.html"

    def get_query(self):
        return Project.objects.filter(members=self.request.user)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "projects/create.html"
    fields = ["name", "description", "members"]

    def form_valid(self, form):
        project = form.save(commit=True)
        return redirect("show_project", pk=project.id)

    def get_context_data(self, **kwargs):
        markdowntext = open(
            os.path.join(os.path.dirname(__file__), "templates/test.md")
        ).read()

        context = super().get_context_data(**kwargs)
        context["markdowntext"] = markdowntext

        return context
