import logging

from channels.layers import get_channel_layer
from django.tasks import task

logger = logging.getLogger(__name__)

@task
async def refresh_channel(channel_name: str) -> None:
    channel_layer = get_channel_layer()
    await channel_layer.group_send(channel_name, {'type': 'refresh'})
