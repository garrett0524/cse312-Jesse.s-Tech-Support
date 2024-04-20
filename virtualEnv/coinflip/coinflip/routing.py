from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/game-list/', consumers.GameListConsumer.as_asgi()),
]