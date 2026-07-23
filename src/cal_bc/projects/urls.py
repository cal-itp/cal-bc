from django.urls import path

from .views.project import ProjectDeleteView, ProjectEditRedirectView, ProjectListView
from .views.project_benefit import project_benefit
from .views.project_download import ProjectDownloadView
from .views.project_subsection import ProjectEditView

urlpatterns = [
    path("", ProjectListView.as_view(), name="projects"),
    path("<int:pk>/edit", ProjectEditRedirectView.as_view(), name="project_edit"),
    path("<int:project_pk>/subsections/<int:pk>/edit", ProjectEditView.as_view(), name="project_subsection_edit"),
    path("<int:pk>/benefit", project_benefit, name="project_benefit"),
    path("<int:pk>/download", ProjectDownloadView.as_view(), name="project_download"),
    path("<int:pk>/delete", ProjectDeleteView.as_view(), name="project_delete"),
]
