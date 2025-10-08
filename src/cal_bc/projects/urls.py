from django.urls import path

from . import views

urlpatterns = [
    path("", views.landings_index, name="index"),
    path("projects/", views.projects_index, name="projects"),
]
