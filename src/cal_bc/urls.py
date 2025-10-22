"""
URL configuration for cal_bc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import azure_auth.views

from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path, re_path
from django.views.static import serve

urlpatterns = [
    path("azure_auth/", include("azure_auth.urls"), name="azure_auth"),
    re_path(r"^accounts/logout/$", LogoutView.as_view(next_page="/"), name="logout"),
    re_path(r"^admin/login/$", azure_auth.views.azure_auth_login),
    path("admin/", admin.site.urls),
    path("", include("cal_bc.projects.urls"), name="landing"),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
