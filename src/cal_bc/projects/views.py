from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    context = {}
    return render(request, "projects/index.html", context)
