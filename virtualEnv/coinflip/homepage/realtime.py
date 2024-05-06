# realtime.py

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def update_game_list(game_list_data):
    channel_layer = get_channel_layer()
    serializable_data = list(game_list_data.values())  # Convert QuerySet to a list of dictionaries
    async_to_sync(channel_layer.group_send)(
        'game_list',
        {
            'type': 'send_game_list',
            'game_list': serializable_data,
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

def update_user_data(user_id, balance_data, wins_data, losses_data):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'user_{user_id}',
        {
            'type': 'send_user_data',
            'balance': balance_data,
            'wins': wins_data,
            'losses': losses_data,
        }
    )

def update_free_money_balance(user_id, balance_data):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'free_money_{user_id}',
        {
            'type': 'send_user_data',
            'user_id': user_id,
            'balance': balance_data,
        }
    )