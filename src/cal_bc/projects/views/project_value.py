from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from cal_bc.projects.models.project import Value


class ProjectValueView(LoginRequiredMixin, DetailView):
    model = Value
    template_name = "values/show.html"

    def get_queryset(self, *args, **kwargs):
        return Value.objects.filter(project_id=self.kwargs["project_pk"])
