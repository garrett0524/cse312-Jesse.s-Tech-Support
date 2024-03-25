from django.contrib import admin
from .models import AuthToken
from .models import AuthToken, Chat_Data


# Register your models here.

admin.site.register(AuthToken)
admin.site.register(Chat_Data)
