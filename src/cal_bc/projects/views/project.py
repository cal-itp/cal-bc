from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from cal_bc.projects.models.project import Project
from cal_bc.projects.forms.project import ProjectForm


class ProjectListView(LoginRequiredMixin, ListView):
    paginate_by = 10
    template_name = "projects/index.html"
    model = Project


class ProjectNewView(LoginRequiredMixin, CreateView):
    template_name = "projects/new.html"
    form_class = ProjectForm
    success_url = "/projects/"
