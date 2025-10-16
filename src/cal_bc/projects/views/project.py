from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from cal_bc.projects.models.project import Project
from cal_bc.projects.forms.project import ProjectForm


class ProjectListView(LoginRequiredMixin, ListView):
    paginate_by = 10
    template_name = "projects/index.html"
    model = Project


class ProjectNewView(LoginRequiredMixin, CreateView):
    template_name = "projects/new.html"
    form_class = ProjectForm
    success_url = "/projects"


class ProjectEditView(LoginRequiredMixin, UpdateView):
    template_name = "projects/edit.html"
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse_lazy("project", kwargs={"pk": self.object.pk})


class ProjectDetailView(LoginRequiredMixin, UpdateView):
    template_name = "projects/show.html"
    model = Project

    def get_form(self, form_class=None):
        return ProjectForm(instance=self.object, disable_fields=True)
