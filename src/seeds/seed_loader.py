import importlib
import logging
import pkgutil

from django.db import transaction

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class SeedLoader:
    def __init__(self, module: str) -> None:
        self.module = module

    @property
    def seed_files(self) -> list[str]:
        return [
            name
            for _, name, is_pkg in pkgutil.iter_modules(self.module.__path__)
            if not is_pkg and name[0] not in "_~"
        ]

    def get_seed_module(self, seed_file: str) -> list[object]:
        return importlib.import_module(f"{self.module.__name__}.{seed_file}")

    def load_seeds(self, targets: list[str] | None = None) -> None:
        if targets is None:
            targets = []
        if targets is None or len(targets) == 0:
            targets = self.seed_files
        with transaction.atomic():
            for seed_file in targets:
                if seed_file in self.seed_files:
                    logger.info(f"Running {seed_file}...")
                    seed_module = self.get_seed_module(seed_file=seed_file)
                    seed_module.Seed().load()

