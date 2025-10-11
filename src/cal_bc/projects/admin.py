from django.contrib import admin
from cal_bc.projects.models.project import Project


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
