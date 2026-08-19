from functools import partial

from django.contrib import admin
from django.db import transaction

from ..tasks import refresh_channel
from .models.project import Project, Value


class ValueInline(admin.TabularInline):
    model = Value
    fields = ('value',)
    readonly_fields=('value',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    inlines = [ValueInline]

    def save_model(self, request, obj, form, change):
        with transaction.atomic():
            super().save_model(request, obj, form, change)
            transaction.on_commit(partial(refresh_channel.enqueue, channel_name=f"user_{obj.user_id}_projects"))


admin.site.register(Project, ProjectAdmin)
