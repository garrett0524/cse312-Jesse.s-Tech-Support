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
    path('upload_profile_picture/', views.upload_profile_picture, name='upload_profile_picture')


]
