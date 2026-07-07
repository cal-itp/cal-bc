from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404

from cal_bc.projects.models.project import Project
from cal_bc.models.models.model import Section, Subsection


class ProjectListView(LoginRequiredMixin, ListView):
    paginate_by = 10
    template_name = "projects/index.html"
    model = Project

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        page = context['page_obj']
        context['elided_page_range'] = page.paginator.get_elided_page_range(page.number, on_each_side=1, on_ends=1)
        return context


class ProjectEditRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs["pk"])

        try:
            subsection = Subsection.objects.filter(section_id__in=Section.objects.filter(version_id=project.version)).first()
        except IndexError:
            raise Http404("No Subsection matches the given query.")

        return reverse_lazy("project_subsection_edit", kwargs={"project_pk": project.id, "pk": subsection.id})
