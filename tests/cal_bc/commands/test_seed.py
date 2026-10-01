import pytest
import tests.fixtures.seeds

from cal_bc.models.models.model import Model


@pytest.mark.django_db(transaction=True)
class TestSeed:
    @pytest.fixture
    def loader(self) -> SeedLoader:
        return SeedLoader(tests.fixtures.seeds)

    def test_seeds_files(self, loader: SeedLoader) -> None:
        assert loader.seed_files == ["001_seed", "002_create_model"]

    def test_load_seeds(self, loader: SeedLoader) -> None:
        loader.load_seeds()
        assert Model.objects.filter(name="Fake Model").count() == 1
