from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.views.generic.edit import UpdateView
from cal_bc.projects.models.project_field import ProjectField
from cal_bc.projects.models.model_section_field import ModelSectionField
from cal_bc.projects.models.model_section import ModelSection
from cal_bc.projects.forms.model_section import ModelSectionForm


ProjectFieldFormset = inlineformset_factory(
    ModelSectionField, ProjectField, fields=["value"]
)


class ProjectSectionEditView(LoginRequiredMixin, UpdateView):
    model = ModelSection
    form_class = ModelSectionForm
    template_name = "project_sections/edit.html"

    def get_context_data(self, **kwargs):
        data = super(ProjectSectionEditView, self).get_context_data(**kwargs)
        formset = None
        if self.request.POST:
            formset = ProjectFieldFormset(self.request.POST, instance=self.object)
            formset.full_clean()
        else:
            formset = ProjectFieldFormset(instance=self.object)
        data["model_section_fields"] = formset
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context["model_section_fields"]
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object()
            formset.save()
        return super(ProjectSectionEditView, self).form_valid(form)
