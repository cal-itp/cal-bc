from io import BytesIO

import pytest
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse_lazy

from cal_bc.models.models.model import (
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
from cal_bc_calculator.calculator import Calculator


@pytest.mark.django_db(transaction=True)
class TestProjectDownloadViews:
    @pytest.fixture
    def user(self, django_user_model) -> User:
        return django_user_model.objects.create_user(username="caltrans")

    @pytest.fixture
    def model(self) -> Model:
        return Model.objects.create(
            name="Testing",
        )

    @pytest.fixture
    def version(self, model: Model) -> Version:
        return Version.objects.create(
            model=model,
            name="1",
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
        return Section.objects.create(version=version, name="Project Info", code="1")

    @pytest.fixture
    def subsection_1A(self, section: Section) -> Subsection:
        return Subsection.objects.create(section=section, name="Project Data", code="A")

    @pytest.fixture
    def general_info_1A_group(self, subsection_1A: Subsection) -> Group:
        return Group.objects.create(subsection=subsection_1A, name="General Information", position=1)

    @pytest.fixture
    def general_info_1A_group_row_1(self, general_info_1A_group: Group) -> Row:
        return Row.objects.create(group=general_info_1A_group)

    @pytest.fixture
    def name_field(self, general_info_1A_group_row_1: Row) -> Field:
        return Field.objects.create(row=general_info_1A_group_row_1, cell="ProjName", name="Project Name")

    @pytest.fixture
    def project_data_1A_group(self, subsection_1A: Subsection) -> Group:
        return Group.objects.create(subsection=subsection_1A, name="Project Location", position=2)

    @pytest.fixture
    def project_data_1A_group_row_1(self, project_data_1A_group: Group) -> Row:
        return Row.objects.create(group=project_data_1A_group, position=1)

    @pytest.fixture
    def project_location_field(self, project_data_1A_group_row_1: Row) -> Field:
        return Field.objects.create(row=project_data_1A_group_row_1, cell="1) Project Information!H12", name="Project Location")

    @pytest.fixture
    def project_data_1A_group_row_2(self, project_data_1A_group: Group) -> Row:
        return Row.objects.create(group=project_data_1A_group, position=2)
    
    @pytest.fixture
    def construction_period_field(self, project_data_1A_group_row_2: Row) -> Field:
        return Field.objects.create(row=project_data_1A_group_row_2, cell="1) Project Information!F14", unit="years", name="Length of Construction Period")

    @pytest.fixture
    def project_data_1A_group_row_3(self, project_data_1A_group: Group) -> Row:
        return Row.objects.create(group=project_data_1A_group, position=3)

    @pytest.fixture
    def one_two_way_field(self, project_data_1A_group_row_3: Row) -> Field:
        return Field.objects.create(row=project_data_1A_group_row_3, cell="1) Project Information!F15", name="One- or Two-Way Data", display_type=FieldDisplayType.NOT_REQUIRED)

    @pytest.fixture
    def subsection_1B(self, section: Section) -> Subsection:
        return Subsection.objects.create(section=section, name="Project Data", code="A")

    @pytest.fixture
    def highway_design_1B_group(self, subsection_1B: Subsection) -> Group:
        return Group.objects.create(subsection=subsection_1B, name="Highway Design")

    @pytest.fixture
    def highway_design_1B_group_row_1(self, highway_design_1B_group: Group) -> Row:
        return Row.objects.create(group=highway_design_1B_group, position=1)

    @pytest.fixture
    def roadway_no_build_field(self, highway_design_1B_group_row_1: Row) -> Field:
        return Field.objects.create(row=highway_design_1B_group_row_1, cell="1) Project Information!G24", name="Roadway Type No Build", position=1)

    @pytest.fixture
    def roadway_build_field(self, highway_design_1B_group_row_1: Row) -> Field:
        return Field.objects.create(row=highway_design_1B_group_row_1, cell="1) Project Information!H24", name="Roadway Type Build", position=2, display_type=FieldDisplayType.READ_ONLY)

    @pytest.fixture
    def subsection_1E(self, section: Section) -> Subsection:
        return Subsection.objects.create(section=section, name="Project Costs", code="E")

    @pytest.fixture
    def summary_1E_group(self, subsection_1E: Subsection) -> Group:
        return Group.objects.create(subsection=subsection_1E, name="Summary", is_summary=True)

    @pytest.fixture
    def summary_1E_group_row(self, summary_1E_group: Group) -> Row:
        return Row.objects.create(group=summary_1E_group, position=1)

    @pytest.fixture
    def total_costs_field(self, summary_1E_group_row: Row) -> Field:
        return Field.objects.create(row=summary_1E_group_row, cell="1) Project Information!AD44", name="Total Costs")

    @pytest.fixture
    def construction_1E_group(self, subsection_1E: Subsection) -> Group:
        return Group.objects.create(subsection=subsection_1E, name="Construction Period Costs")

    @pytest.fixture
    def construction_1E_group_row_1(self, construction_1E_group: Group) -> Row:
        return Row.objects.create(group=construction_1E_group, position=1)

    @pytest.fixture
    def project_support_year_1_field(self, construction_1E_group_row_1: Row) -> Field:
        return Field.objects.create(row=construction_1E_group_row_1, cell="1) Project Information!W15", name="Project Support Year 1")

    @pytest.mark.vcr
    def test_get_project_download(
        self,
        client: Client,
        user: User,
        project: Project,
        name_field: Field,
        project_location_field: Field,
        construction_period_field: Field,
        one_two_way_field: Field,
        roadway_no_build_field: Field,
        roadway_build_field: Field,
        project_support_year_1_field: Field,
        total_costs_field: Field,
    ) -> None:
        ProjectValue.objects.create(
            project=project, field=name_field, value="Monterey LRT"
        )
        ProjectValue.objects.create(
            project=project, field=project_location_field, value="2"
        )
        ProjectValue.objects.create(
            project=project, field=construction_period_field, value="5"
        )
        ProjectValue.objects.create(
            project=project, field=one_two_way_field, value=""
        )
        ProjectValue.objects.create(
            project=project, field=roadway_no_build_field, value="C"
        )
        ProjectValue.objects.create(
            project=project, field=roadway_build_field, value="E"
        )
        ProjectValue.objects.create(
            project=project, field=project_support_year_1_field, value="222"
        )
        ProjectValue.objects.create(
            project=project, field=total_costs_field, value="333"
        )
        client.force_login(user)
        response = client.get(
            reverse_lazy("project_download", kwargs={"pk": project.pk})
        )
        assert response.status_code == 200
        with BytesIO(b"".join(response.streaming_content)) as buffer:
            evaluator = Calculator(buffer).compile()
        assert evaluator.evaluate(name_field.cell) == "Monterey LRT"
        assert evaluator.evaluate(project_location_field.cell) == 2
        assert evaluator.evaluate(construction_period_field.cell) == 5
        assert evaluator.evaluate(one_two_way_field.cell) == 2
        assert evaluator.evaluate(roadway_no_build_field.cell) == "C"
        assert evaluator.evaluate(roadway_build_field.cell) == "C"
        assert evaluator.evaluate(project_support_year_1_field.cell) == 222
        assert evaluator.evaluate(total_costs_field.cell) == 222000.0
