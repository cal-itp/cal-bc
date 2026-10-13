import pytest

from cal_bc.models.models import model
from cal_bc.projects.templatetags.max_attr import max_attr


@pytest.mark.django_db(transaction=True)
class TestMaxAttr:
    @pytest.fixture
    def cal_bc_model(self) -> model.Model:
        return model.Model.objects.create(name="Cal-B/C Sketch", description="Best for early-stage highway or transit projects.", tags=["Transit", "Commuter Rail"])

    @pytest.fixture
    def version(self, cal_bc_model: model.Model) -> model.Version:
        return cal_bc_model.version_set.create(
            name="8.1",
            url="https://dot.ca.gov/-/media/dot-media/programs/transportation-planning/documents/new-state-planning/transportation-economics/cal-bc/2023-cal-bc/2023-non-federal-model/cal-bc-8-1-sketch-a11y.xlsm",
        )

    @pytest.fixture
    def section(self, version: model.Version) -> model.Section:
        return version.section_set.create(name="Project Information", code="1")

    @pytest.fixture
    def subsection(self, section: model.Section) -> model.Subsection:
        return section.subsection_set.create(
            name="Project Data",
            code="A",
        )

    @pytest.fixture
    def group_1(self, subsection: model.Subsection) -> model.Group:
        return subsection.group_set.create(
            name="General Information",
        )

    @pytest.fixture
    def group_2(self, subsection: model.Subsection) -> model.Group:
        return subsection.group_set.create(
            name="Specific Information",
        )

    def test_empty_list(self) -> None:
        assert max_attr([], "column_count") == 0

    def test_one_element(self, group_1: model.Group) -> None:
        group_1.columngroup_set.create().column_set.create()
        assert max_attr([group_1], "column_count") == 1

    def test_two_elements(self, group_1: model.Group, group_2: model.Group) -> None:
        group_1.columngroup_set.create().column_set.create()
        for _ in range(3):
            group_2.columngroup_set.create().column_set.create()
        assert max_attr([group_1, group_2], "column_count") == 3
