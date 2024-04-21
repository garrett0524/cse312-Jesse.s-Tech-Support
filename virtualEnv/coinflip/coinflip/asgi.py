# asgi.py
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import homepage.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coinflip.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            homepage.routing.websocket_urlpatterns
        )
    ),
})