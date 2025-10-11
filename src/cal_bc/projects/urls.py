from django.urls import path
from django.views.generic import TemplateView

from .views.project import ProjectListView, ProjectNewView

urlpatterns = [
    path(
        "", TemplateView.as_view(template_name="landings/index.html"), name="landings"
    ),
    path("projects/", ProjectListView.as_view(), name="projects"),
    path("projects/new", ProjectNewView.as_view(), name="new_project"),
]
