from django.urls import path

from .views.model import (
    ModelListView,
    ProjectCreateView,
)

urlpatterns = [
    path("", ModelListView.as_view(), name="models"),
    path("<int:model_pk>/versions/<int:pk>/projects/new", ProjectCreateView.as_view(), name="model_project_new"),
]
