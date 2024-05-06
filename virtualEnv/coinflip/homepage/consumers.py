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
    

class FreeMoneyConsumer(WebsocketConsumer):
    def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.room_group_name = f'free_money_{self.user_id}'
        
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
        self.accept()
        self.send(json.dumps({'type': 'connection_established'}))
    
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
    
    def receive(self, text_data):
        pass
    
    def send_user_data(self, event):
        self.send(text_data=json.dumps(event))