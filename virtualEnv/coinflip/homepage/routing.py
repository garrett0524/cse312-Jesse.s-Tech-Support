from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/game-list/$', consumers.GameListConsumer.as_asgi()),
    re_path(r'ws/free-money/(?P<user_id>\d+)/$', consumers.FreeMoneyConsumer.as_asgi()),
]