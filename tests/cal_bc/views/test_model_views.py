import pytest

from cal_bc.models.models.model import Model, Version
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse_lazy
from unbrowsed import parse_html, query_by_text


class TestModelViews:
    @pytest.fixture
    def user(self, django_user_model) -> User:
        return django_user_model.objects.create_user(username="caltrans")

    @pytest.fixture
    def model(self) -> Model:
        return Model.objects.create(
            name="Testing",
        )

    @pytest.fixture(autouse=True)
    def version(self, model: Model) -> Version:
        return Version.objects.create(
            model=model,
            name="1",
            url="https://example.com",
        )

    @pytest.fixture(autouse=True)
    def setup(self, client: Client, user: User) -> None:
        client.force_login(user)

    def test_with_models_index(self, client: Client) -> None:
        response = client.get(reverse_lazy("models"))
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Testing v1")
