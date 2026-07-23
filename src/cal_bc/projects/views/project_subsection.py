from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BaseInlineFormSet
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from extra_views import FormSetSuccessMessageMixin, InlineFormSetView

from cal_bc.models.models.model import Field, Subsection
from cal_bc.projects.forms.project import ValueForm
from cal_bc.projects.models.project import Project, Value


def get_field(form):
    if "field" in form.initial and isinstance(form.initial["field"], int):
        return form.initial["field"]
    elif "field" in form.initial:
        return form.initial["field"].pk


class SortedValueInlineFormSet(BaseInlineFormSet):
    def __iter__(self):
        field_id_forms = {get_field(f): f for f in self.forms}
        sorted_field_ids = Field.objects.filter(id__in=field_id_forms.keys()).select_related('row').select_related('row__group').order_by("row__group__position", "row__position", "position").values_list('id')
        return iter([field_id_forms[pk[0]] for pk in sorted_field_ids])


class ProjectEditView(LoginRequiredMixin, FormSetSuccessMessageMixin, InlineFormSetView):
    model = Project
    inline_model = Value
    form_class = ValueForm
    formset_class = SortedValueInlineFormSet
    prefix = "value"
    factory_kwargs = {"can_delete": False}
    template_name = "projects/edit.html"
    success_message = "Project successfully saved!"

    def get_object(self):
        return get_object_or_404(Project, pk=self.kwargs["project_pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subsection"] = get_object_or_404(Subsection, pk=self.kwargs["pk"])
        return context

    def extra_field_set(self):
        return Field.objects.filter(
            row__group__subsection_id=self.kwargs["pk"]
        ).exclude(
            project_value__project_id=self.kwargs["project_pk"]
        ).select_related("row", "row__group")

    def get_initial(self):
        return [{"field": f} for f in self.extra_field_set().all()]

    def get_formset_kwargs(self):
        kwargs = super().get_formset_kwargs()
        kwargs["queryset"] = Value.objects.filter(
            field__row__group__subsection_id=self.kwargs["pk"],
            project_id=self.kwargs["project_pk"]
        )
        return kwargs

    def get_factory_kwargs(self):
        kwargs = super().get_factory_kwargs()
        kwargs["extra"] = self.extra_field_set().count()
        return kwargs

    def get_success_url(self):
        project = get_object_or_404(Project, pk=self.kwargs["project_pk"])
        subsection = get_object_or_404(Subsection, pk=self.kwargs["pk"])
        if self.request.POST.get("step") == "previous" and subsection.previous_subsection:
            subsection = subsection.previous_subsection
        elif self.request.POST.get("step") == "next" and subsection.next_subsection:
            subsection = subsection.next_subsection
        return reverse_lazy("project_subsection_edit", kwargs={"project_pk": project.id, "pk": subsection.id})
