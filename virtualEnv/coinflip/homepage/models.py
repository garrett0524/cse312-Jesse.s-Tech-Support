from django.db import models
from django.contrib.auth.models import User

class Chat_Data(models.Model):
    user = models.CharField(max_length = 50)
    message = models.CharField(max_length = 200)
    likes = models.ManyToManyField(User, related_name='liked_messages')