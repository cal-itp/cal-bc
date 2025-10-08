from django.http import HttpResponse
from django.shortcuts import render


def landings_index(request) -> HttpResponse:
    context = {}
    return render(request, "landings/index.html", context)
