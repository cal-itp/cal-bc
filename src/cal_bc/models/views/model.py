from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from cal_bc.models.models.model import Model, Version
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
