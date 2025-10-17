from django.urls import path
from django.views.generic import TemplateView

from .views.project import (
    ProjectListView,
    ProjectNewView,
    ProjectEditView,
    ProjectDetailView,
)

urlpatterns = [
    path(
        "", TemplateView.as_view(template_name="landings/index.html"), name="landings"
    ),
    path("projects/", ProjectListView.as_view(), name="projects"),
    path("projects/new", ProjectNewView.as_view(), name="project_new"),
    path("projects/<int:pk>/edit", ProjectEditView.as_view(), name="project_edit"),
    path("projects/<int:pk>/show", ProjectDetailView.as_view(), name="project"),
]
