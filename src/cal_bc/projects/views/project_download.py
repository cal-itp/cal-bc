import urllib.request

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.base import ContentFile
from django_downloadview import VirtualDownloadView

from cal_bc.projects.models.project import Project
from cal_bc_calculator.calculator import BytesCalculator


class ProjectDownloadView(LoginRequiredMixin, VirtualDownloadView):
    attachment = True

    def get_file(self):
        project = Project.objects.get(pk=self.kwargs["pk"])
        version = project.version
        value_map = {
            v.field.cell: v.value
            for v in project.input_set.exclude(value="").exclude(field__cell="")
        }
        url = version.url
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        calculator = BytesCalculator(resp.read())
        calculator.write(value_map)
        return ContentFile(calculator.to_bytes(), name=project.version.url.split("/")[-1])
