import logging
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.tasks import task
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)

@task
def refresh_user_projects(user_pk: int) -> None:
    user = User.objects.get(pk=user_pk)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'user_{user.pk}_projects',
        {'type': 'refresh'}
    )
