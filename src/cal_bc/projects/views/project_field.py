from functools import partial

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView

from cal_bc.models.models.model import Field, Subsection
from cal_bc.projects.forms.project import InputForm
from cal_bc.projects.models.project import Input, Project
from cal_bc.projects.tasks import refresh_project_fields
from cal_bc.tasks import refresh_channel


class ProjectSubsectionFieldView(LoginRequiredMixin, UpdateView):
    model = Input
    form_class = InputForm
    template_name = "projects/fields/edit.html"

    def get_prefix(self) -> str:
        return f"field-{self.kwargs['pk']}-input"

    def get_object(self):
        project = get_object_or_404(Project, pk=self.kwargs["project_pk"])
        field = get_object_or_404(Field, pk=self.kwargs["pk"])
        input, _ = project.input_set.get_or_create(field=field, defaults={"value": ""})
        return input

    def refresh_project(self, project: Project, subsection: Subsection) -> None:
        with transaction.atomic():
            transaction.on_commit(partial(refresh_channel.enqueue, channel_name=f"user_{project.user_id}_projects"))
            transaction.on_commit(partial(refresh_channel.enqueue, channel_name=f"user_{project.user_id}_project_{project.pk}_subsection_{subsection.pk}"))
            result = refresh_project_fields.enqueue(project_pk=project.pk)
            if hasattr(result, "db_result"):
                transaction.on_commit(partial(project.refreshtask_set.create, db_task_result=result.db_result))

    def form_valid(self, form):
        subsection = get_object_or_404(Subsection, pk=self.kwargs["subsection_pk"])
        with transaction.atomic():
            self.object = form.save()
            transaction.on_commit(partial(self.refresh_project, project=self.object.project, subsection=subsection))
            return self.render_to_response(self.get_context_data())

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=400)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        data = kwargs["data"].copy()
        data.update({f"{self.get_prefix()}-field": self.object.field})
        kwargs["data"] = data
        return kwargs

    def get_initial(self):
        if self.object and hasattr(self.object, "field"):
            return {"field": self.object.field}
        else:
            return {"field": Field.objects.get(self.kwargs["pk"])}
