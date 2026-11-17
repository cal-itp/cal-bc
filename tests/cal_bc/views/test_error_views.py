import pytest
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import path, reverse_lazy
from unbrowsed import parse_html, query_by_role, query_by_text

from cal_bc import urls as project_urls


def trigger_error_view(request):
    raise RuntimeError("Server Error")

urlpatterns = project_urls.urlpatterns + [path("test-500/", trigger_error_view)]
handler500 = project_urls.handler500


class TestErrorViews:
    @pytest.fixture
    def user(self, django_user_model) -> User:
        return django_user_model.objects.create_user(username="caltrans")

    def test_404_public_view(self, client: Client):
        response = client.get("/coolproject")
        assert response.status_code == 404
        dom = parse_html(response.content)
        assert query_by_role(dom, "heading", name="We can’t find that page")
        assert query_by_text(dom, "The page you're looking for may have been moved, renamed, or doesn't exist. Check the link, or head back to your projects.")
        assert query_by_role(dom, "link", name="Back to home").element.attributes.get("href") == reverse_lazy("landings")

    def test_404_authenticated_view(
            self,
            client: Client,
            user: User,
    ):
        client.force_login(user)
        response = client.get("/projects/0/subsections/0/")
        assert response.status_code == 404
        dom = parse_html(response.content)
        assert query_by_role(dom, "heading", name="We can’t find that page")
        assert query_by_text(dom, "The page you're looking for may have been moved, renamed, or doesn't exist. Check the link, or head back to your projects.")
        assert query_by_role(dom, "link", name="Back to My Projects").element.attributes.get("href") == reverse_lazy("projects")

    @pytest.mark.urls(__name__)
    def test_500_public_view(self, client: Client):
        client.raise_request_exception = False
        
        response = client.get("/test-500/")

        assert response.status_code == 500
        dom = parse_html(response.content)
        assert query_by_role(dom, "heading", name="We could not complete your request")
        assert query_by_text(dom, "Sorry, this is not working properly on our end. We now know about this mistake and are working to fix it.")
        assert query_by_role(dom, "link", name="Back to home").element.attributes.get("href") == reverse_lazy("landings")
        assert query_by_role(dom, "button", name="Reload page")

    @pytest.mark.urls(__name__)
    def test_500_authenticated_view(
            self,
            client: Client,
            user: User,
    ):
        client.raise_request_exception = False
        client.force_login(user)
        response = client.get("/test-500/")
        assert response.status_code == 500
        dom = parse_html(response.content)
        assert query_by_role(dom, "heading", name="We could not complete your request")
        assert query_by_text(dom, "Sorry, this is not working properly on our end. We now know about this mistake and are working to fix it.")
        assert query_by_text(dom, "Changes since you last saved are not recoverable. Check your inputs after you reload.")
        assert query_by_role(dom, "link", name="Back to My Projects").element.attributes.get("href") == reverse_lazy("projects")
        assert query_by_role(dom, "button", name="Reload page")
