from django.contrib import admin

from cal_bc.projects.models.model_version import ModelVersion
from cal_bc.projects.models.project import Project


class ModelVersionAdmin(admin.ModelAdmin):
    pass


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(ModelVersion, ModelVersionAdmin)
admin.site.register(Project, ProjectAdmin)
