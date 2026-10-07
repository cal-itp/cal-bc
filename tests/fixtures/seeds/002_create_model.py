import seeds.seed
from cal_bc.models.models.model import Model


class Seed(seeds.seed.Seed):
    def load(self):
        Model.objects.create(name="Fake Model")
