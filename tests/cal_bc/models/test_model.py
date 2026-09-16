import pytest

from cal_bc.models.models.model import (
    BenefitsGroup,
    BenefitsRow,
    Field,
    FieldDisplayType,
    Group,
    Model,
    Row,
    Section,
    Subsection,
    Value,
    Version,
)


@pytest.mark.django_db(transaction=True)
class TestModel:
    @pytest.fixture()
    def model(self) -> Model:
        return Model.objects.create(name="Cal-B/C Sketch", description="Best for early-stage highway or transit projects.", tags=["Transit", "Commuter Rail"])

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
        return section_1.subsection_set.create(code="A", name="Project Data", description="Some description")

    @pytest.fixture()
    def subsection_1_b(self, section_1: Section) -> Subsection:
        return section_1.subsection_set.create(code="B", name="Highway Information")

    @pytest.fixture()
    def subsection_2_a(self, section_2: Section) -> Subsection:
        return section_2.subsection_set.create(code="A", name="General Settings")

    @pytest.fixture()
    def group(self, subsection_1_a: Subsection) -> Group:
        return subsection_1_a.group_set.create(name="General Information", position=1, description="General description")

    @pytest.fixture()
    def summary_group(self, subsection_1_a: Subsection) -> Group:
        return subsection_1_a.group_set.create(name="Summary", is_summary=True)

    @pytest.fixture()
    def row(self, group: Group) -> Row:
        return group.row_set.create()

    @pytest.fixture()
    def row2(self, group: Group) -> Row:
        return group.row_set.create(name="Roadway Type")

    @pytest.fixture()
    def field(self, row: Row) -> Field:
        return row.field_set.create(name="Highway Free-Flow Speed", cell="FFSpeedNB", display_type=FieldDisplayType.REQUIRED)

    @pytest.fixture()
    def field_with_unit(self, row: Row) -> Field:
        return row.field_set.create(name="Highway Free-Flow Speed", cell="FFSpeedNB", position=1, unit="mph", display_type=FieldDisplayType.REQUIRED)

    @pytest.fixture()
    def field_not_required(self, row: Row) -> Field:
        return row.field_set.create(name="Highway Free-Flow Speed", cell="FFSpeedNB", display_type=FieldDisplayType.NOT_REQUIRED)

    @pytest.fixture()
    def field_read_only(self, row: Row) -> Field:
        return row.field_set.create(name="Highway Free-Flow Speed", cell="FFSpeedNB", display_type=FieldDisplayType.READ_ONLY)

    @pytest.fixture()
    def value(self, field: Field) -> Value:
        return field.value_set.create(
            name="District 4 - Bay Area",
            value="District 4",
            position=1
        )

    @pytest.fixture()
    def benefits_group(self, subsection_1_a: Subsection) -> BenefitsGroup:
        return subsection_1_a.benefitsgroup_set.create(name="Summary", position=1, description="Benefits Summary")

    @pytest.fixture()
    def benefits_row(self, benefits_group: BenefitsGroup) -> BenefitsGroup:
        return benefits_group.benefitsrow_set.create(name="YR 1")

    def test_model_string_representation(self, model: Model):
        assert str(model) == "Cal-B/C Sketch"

    def test_model_description_string_representation(self, model: Model):
        assert str(model.description) == "Best for early-stage highway or transit projects."

    def test_model_tags_list_representation(self, model: Model):
        assert list(model.tags) == ["Transit", "Commuter Rail"]

    def test_model_latest_version(self, model: Model, version: Version):
        assert model.latest_version() == version

    def test_model_latest_version_no_versions(self, model: Model):
        assert model.latest_version() is None

    def test_version_string_representation(self, version: Version):
        assert str(version) == "8.1"

    def test_version_has_form_link(self, version: Version, subsection_1_a: Subsection):
        assert version.has_form_link() is True

    def test_version_has_form_link_false(self, version: Version):
        assert version.has_form_link() is False

    def test_section_string_representation(self, section_1: Section):
        assert str(section_1) == "1 - Project Information"

    def test_next_section(self, section_1: Section, section_2: Section):
        assert section_1.next_section == section_2

    def test_null_next_section(self, section_2: Section):
        assert section_2.next_section is None

    def test_previous_section(self, section_1: Section, section_2: Section):
        assert section_2.previous_section == section_1

    def test_null_previous_section(self, section_1: Section):
        assert section_1.previous_section is None

    def test_subsection_string_representation(self, subsection_1_a: Subsection):
        assert str(subsection_1_a) == "A - Project Data"

    def test_subsection_description(
        self, subsection_1_a: Subsection
    ) -> None:
        assert subsection_1_a.description == "Some description"

    def test_next_subsection(
        self, subsection_1_a: Subsection, subsection_1_b: Subsection
    ):
        assert subsection_1_a.next_subsection == subsection_1_b

    def test_null_next_subsection(self, subsection_2_a: Subsection):
        assert subsection_2_a.next_subsection is None

    def test_previous_subsection(
        self, subsection_1_a: Subsection, subsection_1_b: Subsection
    ):
        assert subsection_1_b.previous_subsection == subsection_1_a

    def test_null_previous_subsection(
        self, subsection_1_a: Subsection, subsection_1_b: Subsection
    ):
        assert subsection_1_a.previous_subsection is None

    def test_next_section_subsection(
        self, subsection_1_b: Subsection, subsection_2_a: Subsection
    ):
        assert subsection_1_b.next_subsection == subsection_2_a

    def test_previous_section_subsection(
        self, subsection_1_b: Subsection, subsection_2_a: Subsection
    ):
        assert subsection_2_a.previous_subsection == subsection_1_b

    def test_summary_group_set(self, subsection_1_a: Subsection, subsection_1_b: Subsection, summary_group: Group):
        subsection_1_a.group_set.create(name="Summary", is_summary=False)
        subsection_1_b.group_set.create(name="Summary", is_summary=True)
        assert list(subsection_1_a.summary_group_set) == [summary_group]

    def test_non_summary_group_set(self, subsection_1_a: Subsection, subsection_1_b: Subsection, group: group):
        subsection_1_a.group_set.create(name="Summary", is_summary=True)
        subsection_1_b.group_set.create(name="Summary", is_summary=False)
        assert list(subsection_1_a.non_summary_group_set) == [group]

    def test_group_string_representation(self, group: Group):
        assert str(group) == "2 - General Information"

    def test_group_description(self, group: Group) -> None:
        assert group.description == "General description"

    def test_column_group_string_representation(self, group: Group):
        column_group = group.columngroup_set.create()
        assert str(column_group) == "Column Group 1"

    def test_column_group_with_name_string_representation(self, group: Group):
        column_group_with_name = group.columngroup_set.create(position=1, name="Initial Costs")
        assert str(column_group_with_name) == "Column Group: 2 - Initial Costs"

    def test_column_string_representation(self, group: Group):
        column_group = group.columngroup_set.create()
        column = column_group.column_set.create(position=1, name="Project Support")
        assert str(column) == "2 - Project Support"

    def test_field_column_string_representation(self, group: Group, field: Field):
        column_group = group.columngroup_set.create()
        column = column_group.column_set.create(position=1, name="Project Support")
        field_column = column.fieldcolumn_set.create(field=field)
        assert str(field_column) == "Field: Highway Free-Flow Speed - Column: Project Support"

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
        assert str(row) == "1"

    def test_row_with_name_string_representation(self, row2: Row):
        assert str(row2) == "1 - Roadway Type"

    def test_field_string_representation(self, field: Field):
        assert str(field) == "1 - Highway Free-Flow Speed"

    def test_field_with_unit(self, field_with_unit: Field):
        assert str(field_with_unit) == "2 - Highway Free-Flow Speed (mph)"

    def test_field_required(self, field: Field):
        assert field.required == True

    def test_field_not_required(self, field_not_required: Field):
        assert field_not_required.required == False

    def test_field_read_only(self, field_read_only: Field):
        assert field_read_only.read_only == True

    def test_summary_field_read_only(self, summary_group: Group):
        row = summary_group.row_set.create()
        field_read_only = row.field_set.create(name="Highway Free-Flow Speed", cell="FFSpeedNB", display_type=FieldDisplayType.READ_ONLY)
        field_required = row.field_set.create(name="Highway Free-Flow Speed", cell="FFSpeedNB", display_type=FieldDisplayType.REQUIRED)
        field_not_required = row.field_set.create(name="Highway Free-Flow Speed", cell="FFSpeedNB", display_type=FieldDisplayType.NOT_REQUIRED)
        assert field_read_only.read_only == True
        assert field_required.read_only == True
        assert field_not_required.read_only == True

    def test_summary_field_not_required(self, summary_group: Group):
        row = summary_group.row_set.create()
        field_read_only = row.field_set.create(name="Highway Free-Flow Speed", cell="FFSpeedNB", display_type=FieldDisplayType.READ_ONLY)
        field_required = row.field_set.create(name="Highway Free-Flow Speed", cell="FFSpeedNB", display_type=FieldDisplayType.REQUIRED)
        field_not_required = row.field_set.create(name="Highway Free-Flow Speed", cell="FFSpeedNB", display_type=FieldDisplayType.NOT_REQUIRED)
        assert field_read_only.required == False
        assert field_required.required == False
        assert field_not_required.required == False

    def test_value_string_representation(self, value: Value):
        assert str(value) == "2 - District 4 - Bay Area"

    def test_subsection_column_count(self, subsection_1_a: Subsection, group: Group, field: Field, field_with_unit: Field) -> None:
        column_group = group.columngroup_set.create()
        column_1 = column_group.column_set.create(name="Test")
        column_1.fieldcolumn_set.create(field=field)
        column_2 = column_group.column_set.create(name="Other Test")
        column_2.fieldcolumn_set.create(field=field_with_unit)
        subsection_1_a.group_set.create(name="Other Group")
        assert subsection_1_a.column_count == 2

    def test_benefits_group_string_representation(self, benefits_group: BenefitsGroup):
        assert str(benefits_group) == "2 - Summary"

    def test_benefits_row_string_representation(self, benefits_row: BenefitsRow):
        assert str(benefits_row) == "1 - YR 1"

    def test_benefits_field_string_representation(self, benefits_row: BenefitsRow):
        benefits_field = benefits_row.benefitsfield_set.create(name="Life-Cycle Cost")
        assert str(benefits_field) == "1 - Life-Cycle Cost"
