from django.test.client import Client
from unbrowsed import parse_html, query_by_role, query_by_text


class TestLandingViews:
    def test_with_landings_index(self, client: Client):
        response = client.get("/")
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Sign in with Microsoft")
    
    def test_404_public_page(self, client: Client):
        response = client.get("/coolproject")
        assert response.status_code == 404
        dom = parse_html(response.content)
        assert query_by_role(dom, "heading", name="We can’t find that page")
        assert query_by_text(dom, "The page you're looking for may have been moved, renamed, or doesn't exist. Check the link, or head back to your projects.")
        assert query_by_role(dom, "link", name="Back to home")