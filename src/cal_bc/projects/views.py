from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


def landings_index(request) -> HttpResponse:
    context = {}
    return render(request, "landings/index.html", context)


@login_required
def projects_index(request) -> HttpResponse:
    context = {}
    return render(request, "projects/index.html", context)
