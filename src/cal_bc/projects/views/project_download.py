import urllib.request

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.base import ContentFile
from django.db.models import Prefetch
from django_downloadview import VirtualDownloadView

from cal_bc.projects.models.project import Input, Project
from cal_bc_calculator.calculator import BytesCalculator


class ProjectDownloadView(LoginRequiredMixin, VirtualDownloadView):
    attachment = True

    def get_file(self):
        project = Project.objects.select_related("version").prefetch_related(
            Prefetch("input_set", queryset=Input.objects.select_related("field"))
        ).get(pk=self.kwargs["pk"])
        version = project.version
        value_map = {
            i.field.cell: i.value
            for i in project.input_set.exclude(value="").exclude(field__cell="")
        }
        url = version.url
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        calculator = BytesCalculator(resp.read())
        calculator.write(value_map)
        return ContentFile(calculator.to_bytes(), name=project.version.url.split("/")[-1])
