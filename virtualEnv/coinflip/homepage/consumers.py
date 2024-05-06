# consumer.py
from channels.generic.websocket import WebsocketConsumer, async_to_sync, AsyncWebsocketConsumer
import json, time

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
    

class FreeMoneyConsumer(AsyncWebsocketConsumer):
    farming_users = {}  # Store the farming users object

    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.room_group_name = 'free_money'
        self.username = self.scope['user'].username  # Get the username from the scope

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        await self.send(json.dumps({'type': 'connection_established'}))

        # Send the current state of farming users to the new user
        await self.send(json.dumps({
            'type': 'initial_state',
            'farming_users': self.farming_users
        }))

        # Broadcast user join event to all users
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_join',
                'user_id': self.user_id,
                'username': self.username,  # Include the username in the event
                'start_time': int(time.time() * 1000),  # Start time in milliseconds
            }
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        # Remove the user from the farming_users object
        if self.user_id in self.farming_users:
            del self.farming_users[self.user_id]

        # Broadcast user leave event to all users
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_leave',
                'user_id': self.user_id,
            }
        )

    async def receive(self, text_data):
        pass

    async def user_join(self, event):
        self.farming_users[event['user_id']] = {
            'username': event['username'],
            'start_time': event['start_time']
        }

        # Send the user join event to the current user only
        await self.send(json.dumps(event))

    async def user_leave(self, event):
        if event['user_id'] in self.farming_users:
            del self.farming_users[event['user_id']]

        # Send the user leave event to the current user only
        await self.send(json.dumps(event))
    