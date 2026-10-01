from cal_bc.models.models.model import Model

class Seed:
    @property
    def model(self) -> Model:
        model, _ = Model.objects.get_or_create(
            name="Cal-B/C Sketch",
            defaults={
                "description": "Best for early-stage highway or transit projects.",
                "tags": ["Transit", "Commuter Rail"]
            },
        )
        return model

    def load(self) -> None:
        self.model.version_set.get_or_create(
            name="8.1",
            defaults={
                "url": "https://dot.ca.gov/-/media/dot-media/programs/transportation-planning/documents/new-state-planning/transportation-economics/cal-bc/2023-cal-bc/2023-non-federal-model/cal-bc-8-1-sketch-a11y.xlsm",
            }
        )
