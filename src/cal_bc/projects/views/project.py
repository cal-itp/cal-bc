from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404

from cal_bc.projects.models.project import Project
from cal_bc.models.models.model import Subsection


class ProjectListView(LoginRequiredMixin, ListView):
    paginate_by = 10
    template_name = "projects/index.html"
    model = Project


class ProjectEditRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs["pk"])
        try:
            subsection = Subsection.objects.filter(section__version=project.version)[0:1].get()
        except Subsection.DoesNotExist:
            raise Http404("No Subsection matches the given query.")
        return reverse_lazy("project_subsection_edit", kwargs={"project_pk": project.pk, "pk": subsection.pk})
