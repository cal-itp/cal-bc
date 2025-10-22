import io
import urllib.request
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.base import ContentFile
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django_downloadview import VirtualDownloadView

from cal_bc.projects.models.project import Project
from cal_bc.projects.forms.project import ProjectForm
from cal_bc_calculator.calculator import Calculator


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


class ProjectDownloadView(VirtualDownloadView):
    attachment = True

    def get_file(self):
        project = Project.objects.get(pk=self.kwargs["pk"])
        model_version = project.model_version
        url = model_version.url
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        calculator = Calculator(io.BytesIO(resp.read()))
        calculator.write(
            {
                # 1) Project Information
                "ProjName": "Testing Project",
                "ProjType": "    HOV Lane Addition",
                "ProjLoc": 1,
                "Construct": 6,
                # Highway design and traffic data
                "GenLanesNB": 2,
                "GenLanesB": 2,
                "HOVLanesNB": 0,
                "HOVLanesB": 2,
                "HOVRest": 2,
                "FFSpeedNB": 65,
                "SegmentNB": 1.1,
                "ADT0": 90_000,
                "ADT1NB": 101_617,
                "ADT1B": 117_490,
                "ADT20NB": 138_405,
                "ADT20B": 148_823,
                "HOVvolNB": 0,
                "HOVvolB": 2_030,
                "PerWeaveB": 0.1,
                "TruckSpeed": 55,
                "AVONonNB": 1.38,
                "AVONonB": 1.65,
                "AVOPeakNB": 1.42,
                "AVOPeakB": 1.7,
                "AVOHovNB": 0,
                "AVOHovB": 2.15,
                "1) Project Information!P11": 150,
                "1) Project Information!P12": 3,
                "1) Project Information!P13": 34,
                "RateGroupNB": "H",
                "RateGroupB": "H",
                "AccStAvgNB": 1.14,
                "AccStAvgB": 0.64,
                "PFatStAvgNB": 0.006,
                "PFatStAvgB": 0.005,
                "PInjStAvgNB": 0.38,
                "PInjStAvgB": 0.321,
                "TAPT1NB": 1_602,
                "TAPT1B": 1_602,
                "TAPT20NB": 3_037,
                "TAPT20B": 4,
                "TVehMi1NB": 8,
                "TVehMi1B": 8,
                "TVehMi20NB": 16,
                "TVehMi20B": 16,
                "TInTimeNBN": 1,
                "TInTimeNBP": 10,
                "TPerHwy": 0,
                "1) Project Information!W15": 775,
                "1) Project Information!W16": 2_500,
                "1) Project Information!W17": 250,
                "1) Project Information!W18": 250,
                "1) Project Information!W19": 250,
                "1) Project Information!W20": 125,
                "1) Project Information!X15": 1_475,
                "1) Project Information!X16": 400,
                "1) Project Information!Y15": 5_000,
                "1) Project Information!Y16": 28_636,
                "1) Project Information!Y17": 40_000,
                "1) Project Information!Y18": 50_000,
                "1) Project Information!Y19": 10_000,
                "1) Project Information!Y20": 10_000,
                "1) Project Information!Z24": 10,
                "1) Project Information!Z25": 10,
                "1) Project Information!Z26": 10,
                "1) Project Information!Z27": 10,
                "1) Project Information!Z28": 10,
                "1) Project Information!Z29": 10,
                "1) Project Information!Z30": 10,
                "1) Project Information!Z31": 10,
                "1) Project Information!Z32": 10,
                "1) Project Information!Z33": 10,
                "1) Project Information!Z34": 10,
                "1) Project Information!Z35": 10,
                "1) Project Information!Z36": 10,
                "1) Project Information!Z37": 10,
                "1) Project Information!Z38": 10,
                "1) Project Information!Z39": 10,
                "1) Project Information!Z40": 10,
                "1) Project Information!Z41": 10,
                "1) Project Information!Z42": 10,
                "1) Project Information!Z43": 10,
                # 2) Model Inputs
                "2) Model Inputs!H13": 0,
                "2) Model Inputs!H32": 0,
                # 3) Results
                "VehOp": "N",
                "Emissions": "N",
            }
        )
        with io.BytesIO() as buffer:
            calculator.save(buffer)
            buffer.seek(0)
            content = buffer.read()
        return ContentFile(content, name="cal-bc-scratch-8-1.xlsm")
