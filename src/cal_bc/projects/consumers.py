from django.core.paginator import Paginator
from channels.generic.websocket import AsyncWebsocketConsumer
from django.template.loader import get_template
from asgiref.sync import sync_to_async

class ProjectsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope['user']

        if not user.is_authenticated:
            await self.close()
            return

        self.user_group = f'user_{user.id}_projects'

        await self.channel_layer.group_add(
            self.user_group,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        user = self.scope['user']

        if user.is_authenticated:
            await self.channel_layer.group_discard(
                self.user_group,
                self.channel_name
            )

    async def refresh(self, event):
        user = self.scope['user']
        paginator = Paginator(user.project_set.all(), 10)
        page_number = self.scope['query_params'].get('page',('1',))[0]
        page = await sync_to_async(paginator.page)(page_number)
        elided_page_range = await sync_to_async(paginator.get_elided_page_range)(page_number, on_each_side=1, on_ends=1)
        template = await sync_to_async(get_template)("projects/_list.html")
        html = await sync_to_async(template.render)(context={'page_obj': page, 'object_list': page.object_list, 'elided_page_range': elided_page_range})
        await self.send(text_data=html)
