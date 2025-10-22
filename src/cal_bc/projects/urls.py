from django.urls import path
from django.views.generic import TemplateView

from .views.project import (
    ProjectListView,
    ProjectNewView,
    ProjectEditView,
    ProjectDetailView,
)

from .views.project_section import ProjectSectionEditView


urlpatterns = [
    path(
        "", TemplateView.as_view(template_name="landings/index.html"), name="landings"
    ),
    path("projects/", ProjectListView.as_view(), name="projects"),
    path("projects/new", ProjectNewView.as_view(), name="new_project"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="project"),
    path("projects/<int:pk>/edit", ProjectEditView.as_view(), name="edit_project"),
    path(
        "projects/<int:project_pk>/sections/<int:pk>/edit",
        ProjectSectionEditView.as_view(),
        name="edit_project_section",
    ),
]
