from django.urls import path

from .views.project import ProjectDeleteView, ProjectsView, ProjectView
from .views.project_download import ProjectDownloadView
from .views.project_subsection import ProjectSubsectionView

urlpatterns = [
    path("", ProjectsView.as_view(), name="projects"),
    path("<int:pk>/", ProjectView.as_view(), name="project"),
    path(
        "<int:project_pk>/subsections/<int:pk>/",
        ProjectSubsectionView.as_view(),
        name="project_subsection",
    ),
    path("<int:pk>/download/", ProjectDownloadView.as_view(), name="project_download"),
    path("<int:pk>/delete/", ProjectDeleteView.as_view(), name="project_delete"),
]
