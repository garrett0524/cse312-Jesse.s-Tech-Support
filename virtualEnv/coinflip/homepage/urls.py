from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register', views.register, name='register'),
    path('login', views.login,name='login'),
    path('chat', views.chat,name='chat'),
    path('chat_messages', views.chat_messages, name='chat_messages'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile_view'),
    path('game/', views.game_view, name='game'),
    path('upload_profile_picture/', views.upload_profile_picture, name='upload_profile_picture'),
    path('lobby/', views.lobby_view, name='lobby'),
    path('create_game/', views.create_game, name='create_game'),
    path('game_list/', views.game_list, name='game_list'),
    path('play_game/<int:game_id>/', views.play_game, name='play_game'),
    path('get_user_data/', views.get_user_data, name='get_user_data'),
    path('get_player_username/<int:player1_id>/', views.get_player_username, name='get_player_username'),
    path('free_money/', views.free_money, name='free_money'),

]
