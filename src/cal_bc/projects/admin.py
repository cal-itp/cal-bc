from functools import partial

from django.contrib import admin
from django.db import transaction

from ..tasks import refresh_channel
from .models.project import Project, Value


class ValueInline(admin.TabularInline):
    model = Value
    fields = ["field_name"]
    readonly_fields = ["field_name"]

    @admin.display(description="Fields", ordering="field__name")
    def field_name(self, obj):
        return f"{obj.field.name}"

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    inlines = [ValueInline]
    list_display = ["project_name", "model_name", "version", "user", "updated_at"]
    list_select_related = ["user", "version", "version__model"]
    search_fields = ["value__value", "version__model__name", "version__name", "user__username"]
    search_help_text = "Search by Project Name, Model, Version, and Username."

    @admin.display(description="Project", ordering="id")
    def project_name(self, obj):
        name_value = obj.value_set.filter(
            field__name="Project Name",
            project_id=obj.id
        ).first()
        return f"{obj.id!s} - {name_value.value}" if name_value else f"{obj.id!s} - <New Project>"

    @admin.display(description="Model", ordering="version__model__name")
    def model_name(self, obj):
        return obj.version.model.name

    def save_model(self, request, obj, form, change):
        with transaction.atomic():
            super().save_model(request, obj, form, change)
            transaction.on_commit(partial(refresh_channel.enqueue, channel_name=f"user_{obj.user_id}_projects"))


admin.site.register(Project, ProjectAdmin)
