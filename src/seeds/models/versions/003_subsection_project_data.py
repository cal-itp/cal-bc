import seeds.seed
from cal_bc.models.models.model import Section


class Seed(seeds.seed.Seed):
    @property
    def section(self) -> Section:
        return Section.objects.get(
            version__model__name="Cal-B/C Sketch",
            version__name="8.1",
            name="Project Information"
        )

    def load(self) -> None:
        self.section.subsection_set.get_or_create(
            name="Project Data",
            defaults={
                "code":"A",
                "guide": """
                    <h2><strong>Setup Help</strong></h2>
                    <p>All fields in this step are required.</p>
                    <p>Click on any field to see specific help and guidance for that input.</p>
                    <h3><strong>Tips</strong></h3>
                    <ul>
                    <li><p>Your work is saved every X minutes.</p></li>
                    <li><p>Use 'Save Draft' to save immediately.</p></li>
                    <li><p>In the navigation menu for Section 1 only, a checkmark will be displayed when all mandatory questions have been completed.</p></li>
                    </ul>
                """
            }
        )
