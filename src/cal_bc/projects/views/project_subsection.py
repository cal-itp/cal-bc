from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from extra_views import InlineFormSetView
from django.forms import BaseInlineFormSet

from cal_bc.models.models.model import Subsection, Field
from cal_bc.projects.models.project import Project, Value
from cal_bc.projects.forms.project import ValueForm


class SortedValueInlineFormSet(BaseInlineFormSet):
    def __iter__(self):
        field_id_forms = {(f.initial['field'] if isinstance(f.initial['field'], int) else f.initial['field'].pk): f for f in self.forms}
        sorted_field_ids = Field.objects.filter(id__in=field_id_forms.keys()).select_related('row').select_related('row__group').order_by("row__group__position", "row__position", "position").values_list('id')
        return iter([field_id_forms[pk[0]] for pk in sorted_field_ids])


class ProjectEditView(LoginRequiredMixin, InlineFormSetView):
    model = Project
    inline_model = Value
    form_class = ValueForm
    formset_class = SortedValueInlineFormSet
    prefix = 'value'
    factory_kwargs = {"can_delete": False}
    template_name = 'projects/edit.html'

    def get_object(self):
        project = get_object_or_404(Project, pk=self.kwargs["project_pk"])
        return project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subsection"] = get_object_or_404(Subsection, pk=self.kwargs["pk"])
        return context

    def extra_field_set(self):
        return Field.objects.filter(
            row__group__subsection_id=self.kwargs["pk"]
        ).exclude(
            id__in=Value.objects.filter(project_id=self.kwargs["project_pk"]).values_list('field_id', flat=True)
        ).select_related('row').select_related('row__group')

    def get_initial(self):
        return [{"field": f} for f in self.extra_field_set().all()]

    def get_factory_kwargs(self):
        kwargs = super().get_factory_kwargs()
        kwargs["extra"] = self.extra_field_set().count()
        return kwargs

    def get_queryset(self):
        return Value.objects.filter(
            project_id=self.kwargs["project_pk"],
            field__row__group__subsection_id=self.kwargs["pk"]
        ).select_related('row').select_related('row__group').all()

    def get_success_url(self):
        project = get_object_or_404(Project, pk=self.kwargs["project_pk"])
        subsection = get_object_or_404(Subsection, pk=self.kwargs["pk"])
        return reverse_lazy("project_subsection_edit", kwargs={"project_pk": project.id, "pk": subsection.id})
