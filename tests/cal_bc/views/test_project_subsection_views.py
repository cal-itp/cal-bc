import pytest
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse_lazy
from unbrowsed import parse_html, query_by_label_text, query_by_role, query_by_text

from cal_bc.models.models.model import (
    Column,
    ColumnGroup,
    Field,
    FieldDisplayType,
    Group,
    Model,
    Row,
    Section,
    Subsection,
    Version,
)
from cal_bc.projects.models.project import Project
from cal_bc.projects.models.project import Value as ProjectValue


@pytest.mark.django_db(transaction=True)
class TestProjectSubsectionViews:
    @pytest.fixture
    def user(self, django_user_model) -> User:
        return django_user_model.objects.create_user(username="caltrans")

    @pytest.fixture
    def model(self) -> Model:
        return Model.objects.create(name="Cal-B/C Sketch")

    @pytest.fixture
    def version(self, model: Model) -> Version:
        return model.version_set.create(
            name="8.1",
            url="https://dot.ca.gov/-/media/dot-media/programs/transportation-planning/documents/new-state-planning/transportation-economics/cal-bc/2023-cal-bc/2023-non-federal-model/cal-bc-8-1-sketch-a11y.xlsm",
        )

    @pytest.fixture
    def project(self, version: Version, user: User) -> Project:
        return Project.objects.create(
            version=version,
            user=user,
        )

    @pytest.fixture
    def section(self, version: Version) -> Section:
        return version.section_set.create(name="Project Information", code="1")

    @pytest.fixture
    def subsection_1A(self, section: Section) -> Subsection:
        return section.subsection_set.create(
            name="Project Data",
            code="A",
            description="This subsection contains the project data.",
        )

    @pytest.fixture
    def general_info_1A_group(self, subsection_1A: Subsection) -> Group:
        return subsection_1A.group_set.create(
            name="General Information",
            position=1
        )

    @pytest.fixture
    def general_info_1A_group_row_1(self, general_info_1A_group: Group) -> Row:
        return general_info_1A_group.row_set.create(
            position=1,
            guide="""
                # Project Name
                Enter a descriptive name for your project.
            """
        )
    @pytest.fixture
    def name_field(self, general_info_1A_group_row_1: Row) -> Field:
        return general_info_1A_group_row_1.field_set.create(name="Project Name", cell="ProjName")

    @pytest.fixture
    def general_info_1A_group_row_2(self, general_info_1A_group: Group) -> Row:
        return general_info_1A_group.row_set.create(position=2)

    @pytest.fixture
    def district_field(self, general_info_1A_group_row_2: Row) -> Field:
        field = general_info_1A_group_row_2.field_set.create(name="District", cell="ProjLoc")
        field.value_set.create(name="District 1", value="1")
        field.value_set.create(name="District 4", value="4")
        return field

    @pytest.fixture
    def project_data_1A_group(self, subsection_1A: Subsection) -> Group:
        return subsection_1A.group_set.create(
            name="Project Data",
            description="Configure project analysis settings.",
            position=2
        )

    @pytest.fixture
    def project_data_1A_group_row(self, project_data_1A_group: Group) -> Row:
        return project_data_1A_group.row_set.create(position=1)

    @pytest.fixture
    def length_peak_period_field(self, project_data_1A_group_row: Row) -> Field:
        return project_data_1A_group_row.field_set.create(name="Length of Peak Period(s)", cell="1) Project Information!F17", display_type=FieldDisplayType.NOT_REQUIRED)

    @pytest.fixture
    def subsection_1E(self, section: Section) -> Subsection:
        return section.subsection_set.create(name="Project Costs", code="E")

    @pytest.fixture
    def summary_1E_group(self, subsection_1E: Subsection) -> Group:
        return subsection_1E.group_set.create(name="Summary", is_summary=True)

    @pytest.fixture
    def summary_1E_group_row(self, summary_1E_group: Group) -> Row:
        return summary_1E_group.row_set.create(position=1)

    @pytest.fixture
    def total_project_support_summary_field(self, summary_1E_group_row: Row) -> Field:
        return summary_1E_group_row.field_set.create(name="Total Project Support", cell="1) Project Information!W44", unit="$", position=1)

    @pytest.fixture
    def total_construction_summary_field(self, summary_1E_group_row: Row) -> Field:
        return summary_1E_group_row.field_set.create(name="Total Construction", cell="1) Project Information!Y44", unit="$", position=2)

    @pytest.fixture
    def costs_1E_group(self, subsection_1E: Subsection) -> Group:
        return subsection_1E.group_set.create(name="Construction Period Costs")

    @pytest.fixture
    def costs_1E_group_project_column_group(self, costs_1E_group: Group) -> ColumnGroup:
        return costs_1E_group.columngroup_set.create(name="Direct Project Initial Costs", position=1)

    @pytest.fixture
    def costs_1E_group_project_column(self, costs_1E_group_project_column_group: ColumnGroup) -> Column:
        return costs_1E_group_project_column_group.column_set.create(name="Project Support", position=1)

    @pytest.fixture
    def costs_1E_group_construction_column(self, costs_1E_group_project_column_group: ColumnGroup) -> Column:
        return costs_1E_group_project_column_group.column_set.create(name="Construction", position=2)

    @pytest.fixture
    def costs_1E_group_costs_column_group(self, costs_1E_group: Group) -> ColumnGroup:
        return costs_1E_group.columngroup_set.create(name="Costs (in Dollars)", position=2)

    @pytest.fixture
    def costs_1E_group_constant_column(self, costs_1E_group_costs_column_group: ColumnGroup) -> Column:
        return costs_1E_group_costs_column_group.column_set.create(name="Constant Dollars", position=1)

    @pytest.fixture
    def costs_1E_group_present_column(self, costs_1E_group_costs_column_group: ColumnGroup) -> Column:
        return costs_1E_group_costs_column_group.column_set.create(name="Present Value", position=2)

    @pytest.fixture
    def costs_1E_group_year_1_row(self, costs_1E_group: Group) -> Row:
        return costs_1E_group.row_set.create(name="Yr 1", position=1)

    @pytest.fixture
    def year_one_project_support_field(self, costs_1E_group_year_1_row: Row, costs_1E_group_project_column: Column) -> Field:
        field = costs_1E_group_year_1_row.field_set.create(name="Project Support Year 1", cell="1) Project Information!W15", position=1, display_type=FieldDisplayType.REQUIRED)
        costs_1E_group_project_column.fieldcolumn_set.create(field=field)
        return field

    @pytest.fixture
    def year_one_construction_field(self, costs_1E_group_year_1_row: Row, costs_1E_group_construction_column: Column) -> Field:
        field = costs_1E_group_year_1_row.field_set.create(name="Construction Year 1", cell="1) Project Information!Y15", position=2, display_type=FieldDisplayType.REQUIRED)
        costs_1E_group_construction_column.fieldcolumn_set.create(field=field)
        return field

    @pytest.fixture
    def year_one_constant_field(self, costs_1E_group_year_1_row: Row, costs_1E_group_constant_column: Column) -> Field:
        field = costs_1E_group_year_1_row.field_set.create(name="Constant Dollars Year 1", cell="1) Project Information!AD15", position=3, unit="$", display_type=FieldDisplayType.READ_ONLY)
        costs_1E_group_constant_column.fieldcolumn_set.create(field=field)
        return field

    @pytest.fixture
    def year_one_present_field(self, costs_1E_group_year_1_row: Row, costs_1E_group_present_column: Column) -> Field:
        field = costs_1E_group_year_1_row.field_set.create(name="Present Value Year 1", cell="1) Project Information!AE15", position=4, unit="$", display_type=FieldDisplayType.READ_ONLY)
        costs_1E_group_present_column.fieldcolumn_set.create(field=field)
        return field

    def test_subsection_edit(
        self,
        client: Client,
        user: User,
        project: Project,
        version: Version,
        subsection_1A: Subsection,
        name_field: Field,
        district_field: Field,
        length_peak_period_field: Field,
    ):
        client.force_login(user)
        response = client.get(
            reverse_lazy(
                "project_subsection",
                kwargs={"project_pk": project.pk, "pk": subsection_1A.pk},
            )
        )
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_role(dom, "heading", name="1A. Project Data")
        assert query_by_text(dom, "This subsection contains the project data.")
        assert query_by_role(dom, "heading", name="General Information")
        assert query_by_role(dom, "heading", name="Project Data")
        assert query_by_text(dom, "Configure project analysis settings.")

        assert query_by_label_text(dom, "Project Name*")
        assert query_by_role(dom, "combobox", name="District*")
        assert query_by_text(dom, "Length of Peak Period(s)")

    def test_summary_table_subsection_edit(
        self,
        client: Client,
        user: User,
        project: Project,
        version: Version,
        subsection_1E: Subsection,
        total_project_support_summary_field: Field,
        total_construction_summary_field: Field,
        year_one_project_support_field: Field,
        year_one_construction_field: Field,
        year_one_constant_field: Field,
        year_one_present_field: Field,
    ):
        client.force_login(user)
        response = client.get(
            reverse_lazy(
                "project_subsection",
                kwargs={"project_pk": project.pk, "pk": subsection_1E.pk},
            )
        )
        assert response.status_code == 200
        dom = parse_html(response.content)
        assert query_by_role(dom, "heading", name="1E. Project Costs")
        assert query_by_role(dom, "heading", name="Construction Period Costs")
        assert query_by_text(dom, "Direct Project Initial Costs")
        assert query_by_text(dom, "Costs (in Dollars)")
        assert query_by_text(dom, "Project Support")
        assert query_by_text(dom, "Construction")
        assert query_by_text(dom, "Constant Dollars")
        assert query_by_text(dom, "Present Value")
        assert query_by_label_text(dom, "Project Support Year 1*")
        assert query_by_label_text(dom, "Construction Year 1*")
        assert query_by_text(dom, "Constant Dollars Year 1")
        assert query_by_text(dom, "Present Value Year 1")

    def test_subsection_edit_submission(
        self,
        client: Client,
        user: User,
        project: Project,
        version: Version,
        subsection_1A: Subsection,
        name_field: Field,
        district_field: Field,
        length_peak_period_field: Field,
    ):
        client.force_login(user)
        response = client.post(
            reverse_lazy(
                "project_subsection",
                kwargs={"project_pk": project.pk, "pk": subsection_1A.pk},
            ),
            data={
                "value-0-field": name_field.pk,
                "value-0-value": "Testing",
                "value-1-field": district_field.pk,
                "value-1-value": "1",
                "value-2-field": length_peak_period_field.pk,
                "value-2-value": "",
                "value-TOTAL_FORMS": 3,
                "value-INITIAL_FORMS": 0,
            },
        )

        assert response.status_code == 302
        assert response.url == reverse_lazy(
            "project_subsection",
            kwargs={"project_pk": project.pk, "pk": subsection_1A.pk},
        )

        assert ProjectValue.objects.filter(field=name_field)[0].value == "Testing"
        assert ProjectValue.objects.filter(field=district_field)[0].value == "1"
        assert ProjectValue.objects.filter(field=length_peak_period_field)[0].value == "5"
