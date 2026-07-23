from django.urls import path
from django.views.generic import RedirectView, TemplateView


def on_authenticated(authenticated_view, unauthenticated_view):
    def switch(request, *args, **kwargs):
        if request.user.is_authenticated:
            return authenticated_view(request, *args, **kwargs)
        else:
            return unauthenticated_view(request, *args, **kwargs)
    return switch

urlpatterns = [
    path(
        "", on_authenticated(
            RedirectView.as_view(pattern_name="projects", permanent=False),
            TemplateView.as_view(template_name="landings/index.html")
        ), name="landings"
    ),
]
