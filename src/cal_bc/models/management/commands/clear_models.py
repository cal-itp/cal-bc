import logging

from django.core.management.base import BaseCommand

from cal_bc.models.models.model import Model

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Clears Models and related records from the database."

    def handle(self, *args, **options):
        logger.info("Deleting all model data")
        Model.objects.all().delete()
