from functools import partial

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Count, Prefetch
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from extra_views import FormSetSuccessMessageMixin, InlineFormSetView

from cal_bc.models.models.model import (
    Column,
    ColumnGroup,
    Field,
    FieldDisplayType,
    Group,
    Row,
    Subsection,
)
from cal_bc.projects.forms.project import InputForm
from cal_bc.projects.models.project import Calculation, Input, Project, RefreshTask
from cal_bc.projects.tasks import refresh_project_fields
from cal_bc.projects.templatetags.max_attr import max_attr
from cal_bc.tasks import refresh_channel


class ProjectSubsectionView(
    LoginRequiredMixin, FormSetSuccessMessageMixin, InlineFormSetView
):
    model = Project
    inline_model = Input
    form_class = InputForm
    factory_kwargs = {"can_delete": False}
    template_name = "projects/edit.html"
    success_message = "Project successfully saved!"

    def get_prefix(self) -> str:
        return f"subsection-{self.kwargs['pk']}-input"

    def get_object(self):
        return get_object_or_404(
            Project.objects.prefetch_related(
                Prefetch("input_set", queryset=Input.objects.select_related("field")),
                Prefetch("calculation_set", queryset=Calculation.objects.select_related("field")),
                Prefetch("refreshtask_set", queryset=RefreshTask.objects.select_related("db_task_result"))
            ),
            pk=self.kwargs["project_pk"]
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        non_table_row_prefetch = Prefetch("row_set", queryset=Row.objects.non_table().order_by("position").annotate(Count("field")), to_attr="non_table_row_set")
        table_row_prefetch = Prefetch(
    "row_set",
            queryset=Row.objects.table().prefetch_related(
                Prefetch("field_set", queryset=Field.objects.input(), to_attr="input_field_set"),
                Prefetch("field_set", queryset=Field.objects.required(), to_attr="required_field_set"),
            )
            .order_by("position")
            .annotate(Count("field"))
        , to_attr="table_row_set")
        column_group_prefetch = Prefetch("columngroup_set", queryset=ColumnGroup.objects.prefetch_related(
            Prefetch("column_set", queryset=Column.objects.prefetch_related("field_set__row__group"))
        ))

        context["subsection"] = get_object_or_404(
            Subsection.objects.prefetch_related(
                "section__version__model",
                Prefetch("group_set", queryset=Group.objects.non_summary().prefetch_related(
                    non_table_row_prefetch,
                    table_row_prefetch,
                    column_group_prefetch,
                ).order_by("position").annotate(column_count=Count("columngroup__column__id")), to_attr="non_summary_group_set"),
                Prefetch("group_set", queryset=Group.objects.summary().prefetch_related(
                    non_table_row_prefetch
                ).order_by("position"), to_attr="summary_group_set")
            ),
            pk=self.kwargs["pk"]
        )

        context["subsection_column_count"] = max_attr(context["subsection"].non_summary_group_set, "column_count")
        return context

    def extra_field_set(self):
        return (
            Field.objects.filter(row__group__subsection_id=self.kwargs["pk"])
            .exclude(display_type=FieldDisplayType.READ_ONLY)
            .exclude(row__group__is_summary=True)
            .exclude(input__project=self.object)
            .select_related("row", "row__group")
            .prefetch_related("fieldrange", "input_set", "calculation_set", "choice_set")
        )

    def get_initial(self):
        return [{"field": f} for f in self.extra_field_set().all()]

    def get_formset_kwargs(self):
        kwargs = super().get_formset_kwargs()
        kwargs["queryset"] = (
            Input.objects
            .filter(project=self.object)
            .filter(field__row__group__subsection_id=self.kwargs["pk"])
            .exclude(field__display_type=FieldDisplayType.READ_ONLY)
            .exclude(field__row__group__is_summary=True)
            .select_related("field__fieldrange", "field__row", "field__row__group")
            .prefetch_related("field__input_set", "field__calculation_set", "field__choice_set")
        )
        return kwargs

    def get_factory_kwargs(self):
        kwargs = super().get_factory_kwargs()
        kwargs["extra"] = self.extra_field_set().count()
        return kwargs

    def refresh_project(self, project: Project, subsection: Subsection) -> None:
        with transaction.atomic():
            transaction.on_commit(partial(refresh_channel.enqueue, channel_name=f"user_{project.user_id}_projects"))
            transaction.on_commit(partial(refresh_channel.enqueue, channel_name=f"user_{project.user_id}_project_{project.pk}_subsection_{subsection.pk}"))
            result = refresh_project_fields.enqueue(project_pk=project.pk)
            if hasattr(result, "db_result"):
                transaction.on_commit(partial(project.refreshtask_set.create, db_task_result=result.db_result))

    def formset_valid(self, formset):
        subsection = get_object_or_404(Subsection, pk=self.kwargs["pk"])
        with transaction.atomic():
            transaction.on_commit(partial(self.refresh_project, project=self.object, subsection=subsection))
            return super().formset_valid(formset)

    def get_success_url(self):
        subsection = get_object_or_404(Subsection.objects.select_related("section__version"), pk=self.kwargs["pk"])
        if (
            self.request.POST.get("step") == "previous"
            and subsection.previous_subsection
        ):
            subsection = subsection.previous_subsection
        elif self.request.POST.get("step") == "next" and subsection.next_subsection:
            subsection = subsection.next_subsection
        return reverse_lazy(
            "project_subsection",
            kwargs={"project_pk": self.object.id, "pk": subsection.id},
        )
