from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register', views.register, name='register'),
    path('login', views.login,name='login'),
    path('chat', views.chat,name='chat'),
    path('chat_messages', views.chat_messages, name='chat_messages'),
    path('logout/', views.logout_view, name='logout'),

]