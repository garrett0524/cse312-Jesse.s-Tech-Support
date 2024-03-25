from django.db import models
from django.contrib.auth.models import User

class AuthToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)

class Chat_Data(models.Model):
    user = models.CharField(max_length = 50)
    message = models.CharField(max_length = 200)
