import logging

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.tasks import task

logger = logging.getLogger(__name__)

@task
def refresh_channel(channel_name: str) -> None:
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(channel_name, {'type': 'refresh'})
