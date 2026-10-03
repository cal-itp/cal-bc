from cal_bc.models.models.model import Model

class Seed:
    def load(self):
        Model.objects.create(name="Fake Model")
