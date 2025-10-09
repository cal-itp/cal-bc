from django.urls import path

from . import views

urlpatterns = [
    path("", views.landings_index, name="landings"),
    path("projects/", views.projects_index, name="projects"),
]
