from channels.generic.websocket import WebsocketConsumer
import json

class GameListConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        pass

    def send_game_list(self, event):
        self.send(text_data=json.dumps(event['game_list']))

    def send_balance(self, event):
        self.send(text_data=json.dumps(event['balance']))