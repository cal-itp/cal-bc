from django.urls import path

from cal_bc.projects.consumers import ProjectsConsumer

websocket_urlpatterns = [
  path("ws/projects/", ProjectsConsumer.as_asgi()),
]
