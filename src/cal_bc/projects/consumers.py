from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.http.request import HttpRequest

from cal_bc.projects.views.project import ProjectsView
from cal_bc.projects.views.project_subsection import ProjectSubsectionView


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
        view = ProjectsView()
        view.template_name = "projects/_list.html"
        request = HttpRequest()
        request.GET['page'] = self.scope['query_params'].get('page',('1',))[0]
        request.user = self.scope['user']
        await sync_to_async(view.setup)(request=request)
        response = await sync_to_async(view.get)(request=request)
        await sync_to_async(response.render)()
        await self.send(text_data=response.content.decode("utf-8"))


class ProjectSubsectionEditConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope['user']
        self.project_pk = self.scope['url_route']['kwargs']['project_pk']
        self.subsection_pk = self.scope['url_route']['kwargs']['pk']

        if not user.is_authenticated:
            await self.close()
            return

        self.user_group = f'user_{user.id}_project_{self.project_pk}_subsection_{self.subsection_pk}'

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
        view = ProjectSubsectionView()
        view.template_name = "projects/_form.html"
        request = HttpRequest()
        request.user = self.scope['user']
        await sync_to_async(view.setup)(request=request, project_pk=self.project_pk, pk=self.subsection_pk)
        response = await sync_to_async(view.get)(request=request, project_pk=self.project_pk, pk=self.subsection_pk)
        await sync_to_async(response.render)()
        await self.send(text_data=response.content.decode("utf-8"))
