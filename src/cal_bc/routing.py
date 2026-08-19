from django.urls import path

from cal_bc.projects.consumers import ProjectsConsumer, ProjectSubsectionConsumer

websocket_urlpatterns = [
  path("ws/projects/", ProjectsConsumer.as_asgi()),
  path("ws/projects/<int:project_pk>/subsections/<int:pk>/", ProjectSubsectionConsumer.as_asgi()),
]
