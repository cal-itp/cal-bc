import os

import pytest

from .channels_live_server_helper import ChannelsLiveServer

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

@pytest.fixture(scope='session')
def channels_live_server(request, live_server):
    server = ChannelsLiveServer()
    request.addfinalizer(server.stop)
    return server
