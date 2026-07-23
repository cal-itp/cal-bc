"""
ASGI config for cal_bc project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
import cal_bc.routing
from urllib.parse import parse_qs

from channels.auth import AuthMiddlewareStack
from channels.middleware import BaseMiddleware
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application


class QueryParamsMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        scope = dict(scope)
        scope["query_params"] = parse_qs(scope["query_string"].decode())
        return await super().__call__(scope, receive, send)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cal_bc.settings")

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": QueryParamsMiddleware(
        AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter(
                    cal_bc.routing.websocket_urlpatterns
                )
            )
        )
    ),
})
