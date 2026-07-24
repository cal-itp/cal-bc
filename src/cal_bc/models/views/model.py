from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from cal_bc.models.models.model import Model, Row, Subsection, Version
from cal_bc.projects.models.project import Project


class ModelListView(LoginRequiredMixin, ListView):
    paginate_by = 10
    template_name = "models/index.html"
    model = Model

    def get_queryset(self):
        return self.model.objects.prefetch_related("version_set").all()


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = []

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.version = Version.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("project_edit", kwargs={"pk": self.object.pk})


class RowGuideView(LoginRequiredMixin, DetailView):
    model = Row
    template_name = "rows/guides/show.html"

    def get_queryset(self, *args, **kwargs):
        return Row.objects.filter(
            group_id=self.kwargs["group_pk"],
            group__subsection_id=self.kwargs["subsection_pk"],
            group__subsection__section_id=self.kwargs["section_pk"],
            group__subsection__section__version_id=self.kwargs["version_pk"],
            group__subsection__section__version__model_id=self.kwargs["model_pk"],
        )


class SubsectionGuideView(LoginRequiredMixin, DetailView):
    model = Subsection
    template_name = "subsections/guides/show.html"

    def get_queryset(self, *args, **kwargs):
        return Subsection.objects.filter(
            section_id=self.kwargs["section_pk"],
            section__version_id=self.kwargs["version_pk"],
            section__version__model_id=self.kwargs["model_pk"],
        )
