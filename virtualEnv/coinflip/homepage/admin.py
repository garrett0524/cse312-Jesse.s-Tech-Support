from django.contrib import admin
from .models import Chat_Data, UserProfile, Player, Game


# Register your models here.

admin.site.register(Chat_Data)
admin.site.register(UserProfile)
admin.site.register(Player)
admin.site.register(Game)
