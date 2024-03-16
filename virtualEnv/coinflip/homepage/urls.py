from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register', views.register, name='register'),
    path('login', views.login,name='login'),
    path('chat', views.chat,name='chat'),

]