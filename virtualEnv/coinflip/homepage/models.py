from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields you need for the user profile
    currency = models.IntegerField(default=100000)
    bio = models.TextField(default="No bio provided")


    # This will display the user's username in the admin panel
    def __str__(self):
        return self.user.username

# When a new user is created, this will also create a new UserProfile for that user, the model above.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

class Chat_Data(models.Model):
    user = models.CharField(max_length = 50)
    message = models.CharField(max_length = 200)
    likes = models.ManyToManyField(User, related_name='liked_messages')
