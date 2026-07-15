from django.urls import path

from .views.model import (
    ModelListView,
    ProjectCreateView,
    RowGuideView,
)

urlpatterns = [
    path("", ModelListView.as_view(), name="models"),
    path("<int:model_pk>/versions/<int:version_pk>/sections/<int:section_pk>/subsections/<int:subsection_pk>/groups/<int:group_pk>/rows/<int:pk>/guide", RowGuideView.as_view(), name="model_version_section_subsection_group_row_guide"),
    path("<int:model_pk>/versions/<int:pk>/projects/new", ProjectCreateView.as_view(), name="model_project_new"),
]
