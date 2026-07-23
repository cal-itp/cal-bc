import pytest
from cal_bc.models.models.model import Model, Version, Section, Subsection, Group, Row, Field, Value


@pytest.mark.django_db
class TestModel:
    @pytest.fixture()
    def model(self) -> Model:
        return Model.objects.create(name="Cal-B/C Sketch")

    @pytest.fixture()
    def version(self, model: Model) -> Version:
        return model.version_set.create(name="8.1", url="https://example.com")

    @pytest.fixture()
    def earlier_version(self, model: Model) -> Version:
        return model.version_set.create(name="8.0", url="https://example.com")

    @pytest.fixture()
    def section_1(self, version: Version) -> Section:
        return version.section_set.create(code="1", name="Project Information")

    @pytest.fixture()
    def section_2(self, version: Version) -> Section:
        return version.section_set.create(code="2", name="Configuration")

    @pytest.fixture()
    def subsection_1_a(self, section_1: Section) -> Subsection:
        return section_1.subsection_set.create(code="A", name="Project Data")

    @pytest.fixture()
    def subsection_1_b(self, section_1: Section) -> Subsection:
        return section_1.subsection_set.create(code="B", name="Highway Information")

    @pytest.fixture()
    def subsection_2_a(self, section_2: Section) -> Subsection:
        return section_2.subsection_set.create(code="A", name="General Settings")

    @pytest.fixture()
    def group(self, subsection_1_a: Subsection) -> Group:
        return subsection_1_a.group_set.create(name="General Information", position=1)

    @pytest.fixture()
    def row(self, group: Group) -> Row:
        return group.row_set.create(position=1)

    @pytest.fixture()
    def field(self, row: Row) -> Field:
        return row.field_set.create(name="District", position=1)

    @pytest.fixture()
    def value(self, field: Field) -> Value:
        return field.value_set.create(
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

    def test_section_string_representation(self, section_1: Section):
        assert str(section_1) == "Cal-B/C Sketch v8.1 § 1 Project Information"

    def test_next_section(self, section_1: Section, section_2: Section):
        assert section_1.next_section == section_2

    def test_null_next_section(self, section_2: Section):
        assert section_2.next_section is None

    def test_previous_section(self, section_1: Section, section_2: Section):
        assert section_2.previous_section == section_1

    def test_null_previous_section(self, section_1: Section):
        assert section_1.previous_section is None

    def test_subsection_string_representation(self, subsection_1_a: Subsection):
        assert str(subsection_1_a) == "Cal-B/C Sketch v8.1 § 1A Project Data"

    def test_next_subsection(self, subsection_1_a: Subsection, subsection_1_b: Subsection):
        assert subsection_1_a.next_subsection == subsection_1_b

    def test_null_next_subsection(self, subsection_2_a: Subsection):
        assert subsection_2_a.next_subsection is None

    def test_previous_subsection(self, subsection_1_a: Subsection, subsection_1_b: Subsection):
        assert subsection_1_b.previous_subsection == subsection_1_a

    def test_null_previous_subsection(self, subsection_1_a: Subsection, subsection_1_b: Subsection):
        assert subsection_1_a.previous_subsection is None

    def test_next_section_subsection(self, subsection_1_b: Subsection, subsection_2_a: Subsection):
        assert subsection_1_b.next_subsection == subsection_2_a

    def test_previous_section_subsection(self, subsection_1_b: Subsection, subsection_2_a: Subsection):
        assert subsection_2_a.previous_subsection == subsection_1_b

    def test_group_string_representation(self, group: Group):
        assert str(group) == "Cal-B/C Sketch v8.1 § 1A General Information"

    def test_group_table_row_set_empty(self, group: Group):
        assert list(group.table_row_set.all()) == []

    def test_group_table_row_set(self, group: Group, row: Row, field: Field):
        column_group = group.columngroup_set.create()
        column = column_group.column_set.create(name="Test")
        column.fieldcolumn_set.create(field=field)
        assert list(group.table_row_set.all()) == [row]

    def test_group_non_table_row_set(self, group: Group, row: Row):
        assert list(group.non_table_row_set.all()) == [row]

    def test_group_non_table_row_set_empty(self, group: Group, field: Field):
        column_group = group.columngroup_set.create()
        column = column_group.column_set.create(name="Test")
        column.fieldcolumn_set.create(field=field)
        assert list(group.non_table_row_set.all()) == []

    def test_row_string_representation(self, row: Row):
        assert str(row) == "Cal-B/C Sketch v8.1 § 1A Row 1"

    def test_field_string_representation(self, field: Field):
        assert str(field) == "Cal-B/C Sketch v8.1 § 1A District"

    def test_value_string_representation(self, value: Value):
        assert str(value) == "District 4 - Bay Area"
