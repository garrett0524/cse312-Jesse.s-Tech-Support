# realtime.py

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def update_game_list(game_list_data):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'game_list',
        {
            'type': 'send_game_list',
            'game_list': game_list_data,
        }
    )

def update_balance(user_id, balance_data):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'balance_{user_id}',
        {
            'type': 'send_balance',
            'balance': balance_data,
        }
    )