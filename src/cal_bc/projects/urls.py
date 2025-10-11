from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("projects/", views.projects_index, name="projects"),
    path(
        "", TemplateView.as_view(template_name="landings/index.html"), name="landings"
    ),
]
