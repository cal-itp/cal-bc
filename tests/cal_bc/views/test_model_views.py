import pytest
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse_lazy
from unbrowsed import parse_html, query_by_text

from cal_bc.models.models.model import (
    Field,
    Group,
    Model,
    Row,
    Section,
    Subsection,
    Version,
)


@pytest.mark.django_db(transaction=True)
class TestModelViews:
    @pytest.fixture
    def user(self, django_user_model) -> User:
        return django_user_model.objects.create_user(
            username="caltrans", first_name="John", last_name="Luis"
        )

    @pytest.fixture
    def model(self) -> Model:
        return Model.objects.create(name="Testing", description="Use this model for testing!")

    @pytest.fixture(autouse=True)
    def version(self, model: Model) -> Version:
        return model.version_set.create(name="1", url="https://dot.ca.gov/-/media/dot-media/programs/transportation-planning/documents/new-state-planning/transportation-economics/cal-bc/2023-cal-bc/2023-non-federal-model/cal-bc-8-1-sketch-a11y.xlsm")

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
        return group.row_set.create()

    @pytest.fixture
    def field(self, row: Row) -> Field:
        return row.field_set.create(name="State", cell="1) Project Information!F2")


    @pytest.fixture(autouse=True)
    def setup(self, client: Client, user: User) -> None:
        client.force_login(user)

    def test_models_index(self, client: Client) -> None:
        response = client.get(reverse_lazy("models"))
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Welcome, John")
        assert query_by_text(dom, "Testing v1")
        assert query_by_text(dom, "Use this model for testing!")

    @pytest.mark.vcr
    def test_project_create(self, client: Client, model: Model, version: Version, field: Field) -> None:
        field.choice_set.create(name="California", value="California", is_selected=True)
        field.choice_set.create(name="Florida", value="Florida")

        response = client.post(
            reverse_lazy(
                "model_project_new",
                kwargs={"model_pk": model.pk, "pk": version.pk},
            )
        )

        assert response.status_code == 302
        assert field.input_set.count() == 1
        assert field.input_set.first().value == "California"

    def test_row_guide(
        self,
        client: Client,
        model: Model,
        version: Version,
        section: Section,
        subsection: Subsection,
        group: Group,
        row: Row,
    ) -> None:
        row.guide = "Enter some names here"
        row.save()
        response = client.get(
            reverse_lazy(
                "model_version_section_subsection_group_row_guide",
                kwargs={
                    "model_pk": model.pk,
                    "version_pk": version.pk,
                    "section_pk": section.pk,
                    "subsection_pk": subsection.pk,
                    "group_pk": group.pk,
                    "pk": row.pk,
                },
            )
        )
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Guide")
        assert query_by_text(dom, "Enter some names here")

    def test_row_guide_empty(
        self,
        client: Client,
        model: Model,
        version: Version,
        section: Section,
        subsection: Subsection,
        group: Group,
        row: Row,
    ) -> None:
        response = client.get(
            reverse_lazy(
                "model_version_section_subsection_group_row_guide",
                kwargs={
                    "model_pk": model.pk,
                    "version_pk": version.pk,
                    "section_pk": section.pk,
                    "subsection_pk": subsection.pk,
                    "group_pk": group.pk,
                    "pk": row.pk,
                },
            )
        )
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert not query_by_text(dom, "Guide")

    def test_subsection_guide(
        self,
        client: Client,
        model: Model,
        version: Version,
        section: Section,
        subsection: Subsection,
    ) -> None:
        subsection.guide = "Good information here"
        subsection.save()
        response = client.get(
            reverse_lazy(
                "model_version_section_subsection_guide",
                kwargs={
                    "model_pk": model.pk,
                    "version_pk": version.pk,
                    "section_pk": section.pk,
                    "pk": subsection.pk,
                },
            )
        )
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_text(dom, "Guide")
        assert query_by_text(dom, "Good information here")

    def test_subsection_guide_empty(
        self,
        client: Client,
        model: Model,
        version: Version,
        section: Section,
        subsection: Subsection,
    ) -> None:
        response = client.get(
            reverse_lazy(
                "model_version_section_subsection_guide",
                kwargs={
                    "model_pk": model.pk,
                    "version_pk": version.pk,
                    "section_pk": section.pk,
                    "pk": subsection.pk,
                },
            )
        )
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert not query_by_text(dom, "Guide")
