import pytest
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse_lazy
from unbrowsed import parse_html, query_by_text

from cal_bc.models.models.model import Group, Model, Row, Section, Subsection, Version


class TestModelViews:
    @pytest.fixture
    def user(self, django_user_model) -> User:
        return django_user_model.objects.create_user(username="caltrans", first_name="John", last_name="Luis")

    @pytest.fixture
    def model(self) -> Model:
        return Model.objects.create(name="Testing")

    @pytest.fixture(autouse=True)
    def version(self, model: Model) -> Version:
        return model.version_set.create(name="1", url="https://example.com")

    @pytest.fixture
    def section(self, version: Version) -> Section:
        return version.section_set.create(name="Data", code="1")

    @pytest.fixture
    def subsection(self, section: Section) -> Subsection:
        return section.subsection_set.create(name="Information", code="A")

    @pytest.fixture
    def group(self, subsection: Subsection) -> Group:
        return subsection.group_set.create(name="Basic")

    @pytest.fixture
    def row(self, group: Group) -> Row:
        return group.row_set.create(name="Name")

    @pytest.fixture(autouse=True)
    def setup(self, client: Client, user: User) -> None:
        client.force_login(user)

    def test_models_index(self, client: Client) -> None:
        response = client.get(reverse_lazy("models"))
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Welcome, John")
        assert query_by_text(dom, "Testing v1")

    def test_row_guide(self, client: Client, model: Model, version: Version, section: Section, subsection: Subsection, group: Group, row: Row) -> None:
        row.guide="Enter some names here"
        row.save()
        response = client.get(reverse_lazy("model_version_section_subsection_group_row_guide", kwargs={"model_pk":model.pk, "version_pk":version.pk, "section_pk":section.pk, "subsection_pk":subsection.pk, "group_pk":group.pk, "pk":row.pk}))
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Guide")
        assert query_by_text(dom, "Enter some names here")

    def test_row_guide_empty(self, client: Client, model: Model, version: Version, section: Section, subsection: Subsection, group: Group, row: Row) -> None:
        response = client.get(reverse_lazy("model_version_section_subsection_group_row_guide", kwargs={"model_pk":model.pk, "version_pk":version.pk, "section_pk":section.pk, "subsection_pk":subsection.pk, "group_pk":group.pk, "pk":row.pk}))
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert not query_by_text(dom, "Guide")

    def test_subsection_guide(self, client: Client, model: Model, version: Version, section: Section, subsection: Subsection) -> None:
        subsection.guide="Good information here"
        subsection.save()
        response = client.get(reverse_lazy("model_version_section_subsection_guide", kwargs={"model_pk":model.pk, "version_pk":version.pk, "section_pk":section.pk, "pk":subsection.pk}))
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Guide")
        assert query_by_text(dom, "Good information here")

    def test_subsection_guide_empty(self, client: Client, model: Model, version: Version, section: Section, subsection: Subsection) -> None:
        response = client.get(reverse_lazy("model_version_section_subsection_guide", kwargs={"model_pk":model.pk, "version_pk":version.pk, "section_pk":section.pk, "pk":subsection.pk}))
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert not query_by_text(dom, "Guide")
