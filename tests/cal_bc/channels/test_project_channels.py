from functools import update_wrapper

import pytest
import pytest_asyncio
from asgiref.sync import sync_to_async
from channels.layers import get_channel_layer
from channels.testing import WebsocketCommunicator
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from selectolax.lexbor import LexborHTMLParser as Parser
from unbrowsed import Result, parse_html, query_by_text
from unbrowsed.matchers import TextMatch
from unbrowsed.utils import get_selector

from cal_bc.asgi import application
from cal_bc.models.models.model import (
    Field,
    Group,
    Model,
    Row,
    Section,
    Subsection,
    Version,
)
from cal_bc.projects.models.project import Project


def query_all_by_text(dom: Parser, text: str, exact=True) -> list[Result]:
    search_text = TextMatch(text, exact=exact)
    matches = []

    for element in dom.css(get_selector()):
        element_text = element.text(deep=True, strip=True)

        if search_text.matches(element_text):
            matches.append(Result(element))

    return matches


class AuthWebsocketCommunicator(WebsocketCommunicator):
    def __init__(self, application, path, user, *args, **kwargs):
        super().__init__(self._asgi_with_user(application, user), path,
                         *args, **kwargs)

    @classmethod
    def _asgi_with_user(cls, asgi_app, user):
        async def app(scope, receive, send):
            scope['user'] = user
            return await asgi_app(scope, receive, send)
        update_wrapper(app, asgi_app)
        return app


@pytest.mark.django_db(transaction=True)
class TestProjectChannels:
    @pytest_asyncio.fixture
    async def user(self, django_user_model) -> User:
        yield django_user_model.objects.create_user(
            username="caltrans", first_name="Maria", last_name="Mary"
        )

    @pytest_asyncio.fixture
    async def model(self) -> Model:
        yield Model.objects.create(
            name="Testing",
        )

    @pytest_asyncio.fixture
    async def version(self, model: Model) -> Version:
        yield Version.objects.create(
            model=model,
            name="1",
            url="https://dot.ca.gov/-/media/dot-media/programs/transportation-planning/documents/new-state-planning/transportation-economics/cal-bc/2023-cal-bc/2023-non-federal-model/cal-bc-8-1-sketch-a11y.xlsm",
        )

    @pytest_asyncio.fixture
    async def project(self, version: Version, user: User) -> Project:
        yield version.project_set.create(user=user)

    @pytest_asyncio.fixture
    async def section(self, version: Version) -> Section:
        yield version.section_set.create(name="Project Info", code="1")

    @pytest_asyncio.fixture
    async def subsection(self, section: Section) -> Subsection:
        yield section.subsection_set.create(
            name="Project Data",
            code="A",
            description="Project Data description",
        )

    @pytest_asyncio.fixture
    async def group(self, subsection: Subsection) -> Group:
        yield subsection.group_set.create(
            name="General Information",
            description="General Information description",
        )

    @pytest_asyncio.fixture
    async def row(self, group: Group) -> Row:
        yield group.row_set.create()

    @pytest_asyncio.fixture
    async def name_field(self, row: Row) -> Field:
        yield row.field_set.create(cell="ProjName", name="Project Name")

    @pytest.mark.asyncio
    async def test_project_subsection_edit_refresh(self, user: User, project: Project, subsection: Subsection, name_field: Field) -> None:
        communicator = AuthWebsocketCommunicator(
            application,
            path=f"/ws{reverse_lazy('project_subsection', kwargs={'project_pk': project.pk, 'pk': subsection.pk})}",
            headers=[(b'origin', b'http://localhost:80')],
            user=user,
        )
        connected, _ = await communicator.connect()
        assert connected

        channel_layer = get_channel_layer()
        await channel_layer.group_send(
            f'project_{project.pk}_subsection_{subsection.pk}',
            {'type': 'refresh'}
        )

        response = await communicator.receive_from()
        dom = await sync_to_async(parse_html)(response)

        assert await sync_to_async(query_by_text)(dom, "General Information description")

        await communicator.disconnect()

    @pytest.mark.asyncio
    async def test_projects_refresh(self, user: User, project: Project, subsection: Subsection, name_field: Field) -> None:
        communicator = AuthWebsocketCommunicator(
            application,
            path=f"/ws{reverse_lazy("projects")}",
            headers=[(b'origin', b'http://localhost:80')],
            user=user,
        )
        connected, _ = await communicator.connect()
        assert connected

        channel_layer = get_channel_layer()
        await channel_layer.group_send(f'user_{user.pk}_projects', {'type': 'refresh'})

        response = await communicator.receive_from()
        dom = await sync_to_async(parse_html)(response)

        assert await sync_to_async(query_all_by_text)(dom, "New Project")
        assert await sync_to_async(query_by_text)(dom, "Testing v1")

        await communicator.disconnect()
