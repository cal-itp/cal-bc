import pytest
from cal_bc.models.models.model import Model, Version, Section, Subsection, Group, Row, Field, Value


@pytest.mark.django_db
class TestModels:
    @pytest.fixture()
    def model(self) -> Model:
        return Model.objects.create(
            name="Cal-B/C Sketch",
        )

    @pytest.fixture()
    def version(self, model: Model) -> Version:
        return Version.objects.create(
            model=model,
            name="8.1",
            url="https://example.com",
        )

    @pytest.fixture()
    def earlier_version(self, model: Model) -> Version:
        return Version.objects.create(
            model=model,
            name="8.0",
            url="https://example.com",
        )

    @pytest.fixture()
    def section(self, version: Version) -> Section:
        return Section.objects.create(
            version=version,
            code="1",
            name="Project Information"
        )

    @pytest.fixture()
    def subsection(self, section: Section) -> Subsection:
        return Subsection.objects.create(
            section=section,
            code="A",
            name="Project Data"
        )

    @pytest.fixture()
    def group(self, subsection: Subsection) -> Group:
        return Group.objects.create(
            subsection=subsection,
            name="General Information",
            position=1
        )

    @pytest.fixture()
    def row(self, group: Group) -> Row:
        return Row.objects.create(
            group=group,
            position=1
        )

    @pytest.fixture()
    def field(self, row: Row) -> Field:
        return Field.objects.create(
            row=row,
            name="District",
            position=1
        )

    @pytest.fixture()
    def value(self, field: Field) -> Value:
        return Value.objects.create(
            field=field,
            name="District 4 - Bay Area",
            value="District 4",
            position=1
        )

    def test_model_string_representation(self, model: Model):
        assert str(model) == "Cal-B/C Sketch"

    def test_model_latest_version(self, model: Model, version: Version):
        assert model.latest_version() == version

    def test_model_latest_version_no_versions(self, model: Model):
        assert model.latest_version() is None

    def test_version_string_representation(self, version: Version):
        assert str(version) == "Cal-B/C Sketch v8.1"

    def test_section_string_representation(self, section: Section):
        assert str(section) == "Cal-B/C Sketch v8.1 § 1 Project Information"

    def test_subsection_string_representation(self, subsection: Subsection):
        assert str(subsection) == "Cal-B/C Sketch v8.1 § 1A Project Data"

    def test_group_string_representation(self, group: Group):
        assert str(group) == "Cal-B/C Sketch v8.1 § 1A General Information"

    def test_row_string_representation(self, row: Row):
        assert str(row) == "Cal-B/C Sketch v8.1 § 1A Row 1"

    def test_field_string_representation(self, field: Field):
        assert str(field) == "Cal-B/C Sketch v8.1 § 1A District"

    def test_value_string_representation(self, value: Value):
        assert str(value) == "District 4 - Bay Area"
