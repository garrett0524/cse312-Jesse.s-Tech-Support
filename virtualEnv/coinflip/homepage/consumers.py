# consumer.py
from channels.generic.websocket import WebsocketConsumer, async_to_sync
import json

class GameListConsumer(WebsocketConsumer):
    room_group_name = 'game_list'

    def connect(self):
        self.accept()
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def send_game_list(self, event):
        # Send updated game list to the client
        self.send(text_data=json.dumps(event))

    def send_balance(self, event):
        # Send updated balance to the client
        self.send(text_data=json.dumps(event))