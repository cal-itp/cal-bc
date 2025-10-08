from django.urls import path

from . import views

urlpatterns = [path("", views.landings_index, name="index")]
