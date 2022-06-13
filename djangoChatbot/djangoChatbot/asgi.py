"""
ASGI config for djangoChatbot project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application

import chatapplication.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoChatbot.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chatapplication.routing.websocket_urlpatterns
        )
    )
})
