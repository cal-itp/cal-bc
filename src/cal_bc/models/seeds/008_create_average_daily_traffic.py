from functools import cached_property
from cal_bc.models.models.model import Subsection

class Seed:
    @cached_property
    def subsection(self) -> Subsection:
        return Subsection.objects.get(
            section__version__model__name="Cal-B/C Sketch",
            section__version__name="8.1",
            section__name="Project Data",
            name="Highway Design"
        )

    def load(self) -> None:
        group = self.subsection.group_set.get_or_create(
            name="Average Daily Traffic",
            defaults={"position": 2}
        )

        column_group = group.columngroup_set.get_or_create(position=1)
        column_no_build = column_group.column_set.get_or_create(name="No Build", defaults={"position": 1})
        column_build = column_group.column_set.get_or_create(name="Build", defaults={"position": 2})

        row_1 = group.row_set.get_or_create(position=1, defaults={"name": "Current"})
        field_project_type = row_1.field_set.get_or_create(name="Current", defaults={"cell": "ADT0"})

        row_2 = group.row_set.get_or_create(position=2, defaults={"name": "Base (Year 1)"})
        column_no_build.fieldcolumn_set.create(
            field=row_2.field_set.get_or_create(name="Base (Year 1) No Build", defaults={"cell": "ADT1NB"})
        )
        column_build.fieldcolumn_set.create(
            field=row_2.field_set.get_or_create(name="Base (Year 1) Build", defaults={"cell": "ADT1B"})
        )

        row_3 = group.row_set.get_or_create(position=2, defaults={"name": "Forecast (Year 20)"})
        column_no_build.fieldcolumn_set.create(
            field=row_3.field_set.get_or_create(name="Forecast (Year 20) No Build", defaults={"cell": "ADT20NB"})
        )
        column_build.fieldcolumn_set.create(
            field=row_3.field_set.get_or_create(name="Forecast (Year 20) Build", defaults={"cell": "ADT20B"})
        )
