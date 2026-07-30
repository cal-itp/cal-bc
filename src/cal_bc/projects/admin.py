from functools import partial

from django.contrib import admin
from django.db import transaction

from ..tasks import refresh_channel
from .models.project import Project


class ProjectAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        with transaction.atomic():
            super().save_model(request, obj, form, change)
            transaction.on_commit(partial(refresh_channel.enqueue, channel_name=f"user_{obj.user_id}_projects"))


admin.site.register(Project, ProjectAdmin)
