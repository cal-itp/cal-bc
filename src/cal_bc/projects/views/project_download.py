from functools import cached_property

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.base import ContentFile
from django.db.models import Prefetch
from django_downloadview import VirtualDownloadView

from cal_bc.models.models.model import Version
from cal_bc.models.tasks import refresh_version_file
from cal_bc.projects.models.project import Input, Project
from cal_bc_calculator.calculator import BytesCalculator


class RemoteWorkbook:
    def __init__(self, version: Version) -> None:
        self.version = version

    @cached_property
    def file(self) -> bytes:
        if not hasattr(self.version, "versionfile"):
            refresh_version_file.func(version_pk=self.version.pk)
            self.version.refresh_from_db()
        with self.version.versionfile.file.open() as f:
            return f.read()

    @cached_property
    def calculator(self) -> BytesCalculator:
        return BytesCalculator(self.file)

    def set_cell_values(self, cell_values: dict[str, any]) -> None:
        self.calculator.write(cell_values)

    def read_cell_values(self, cells: list[str]) -> dict[str, any]:
        return {k: v for k, v in zip(cells, self.calculator.evaluate(cells))}

    @property
    def filename(self) -> str:
        return self.version.versionfile.file.name


class ProjectDownloadView(LoginRequiredMixin, VirtualDownloadView):
    attachment = True

    def get_file(self):
        project = Project.objects.select_related("version").prefetch_related(
            Prefetch("input_set", queryset=Input.objects.select_related("field"))
        ).get(pk=self.kwargs["pk"])
        remote_workbook = RemoteWorkbook(version=project.version)
        remote_workbook.set_cell_values({
            i.field.cell: i.value
            for i in project.input_set.exclude(value="").exclude(field__cell="")
        })
        return ContentFile(
            remote_workbook.calculator.to_bytes(),
            name=remote_workbook.filename
        )
