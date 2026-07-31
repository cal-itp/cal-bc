import io
import urllib.request

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.base import ContentFile
from django_downloadview import VirtualDownloadView

from cal_bc.projects.models.project import Project
from cal_bc_calculator.calculator import Calculator


class ProjectDownloadView(LoginRequiredMixin, VirtualDownloadView):
    attachment = True

    def get_file(self):
        project = Project.objects.get(pk=self.kwargs["pk"])
        version = project.version
        value_map = {v.field.cell: v.value for v in project.value_set.all()}
        url = version.url
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        calculator = Calculator(io.BytesIO(resp.read()))
        calculator.write(value_map)
        with io.BytesIO() as buffer:
            calculator.save(buffer)
            buffer.seek(0)
            content = buffer.read()
        return ContentFile(content, name="cal-bc-sketch-8-1.xlsm")
