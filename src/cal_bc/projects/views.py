from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from .models import Project


def index(request) -> HttpResponse:
    context = {}
    return render(request, "projects/index.html", context)


def show(request, project_id: int) -> HttpResponse:
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    return render(request, "projects/show.html", {"project": project})
