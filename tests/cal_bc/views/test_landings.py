from unbrowsed import parse_html, query_by_text


class TestLandingsViews:
    def test_with_landings_index(self, client):
        response = client.get("/")
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Sign in with Microsoft")
