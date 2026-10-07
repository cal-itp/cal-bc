import logging

from django.core.management.base import BaseCommand

import seeds.models.versions
from seeds.seed_loader import SeedLoader

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Command(BaseCommand):
    """
    $ uv run manage.py seed
    """
    help = "Seed the database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument("--target", nargs="+", type=str, help="Name of the seed file to run (e.g. 001_create_model)")

    def handle(self, *args, **kwargs):
        logger.info("Loading seeds...")
        SeedLoader(seeds.models.versions).load_seeds(targets=kwargs["target"])
        logger.info("Finished loading seeds!")
