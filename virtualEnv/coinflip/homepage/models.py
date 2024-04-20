from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currency = models.IntegerField(default=100000)
    bio = models.TextField(default="No bio provided")
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    wins = models.IntegerField(default= 0)
    loses = models.IntegerField(default= 0)


    # This will display the user's username in the admin panel
    def __str__(self):
        return self.user.username

# When a new user is created, this will also create a new UserProfile for that user
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs): #
    if created:
        UserProfile.objects.create(user=instance)

class Chat_Data(models.Model):
    user = models.CharField(max_length = 50)
    message = models.CharField(max_length = 200)
    likes = models.ManyToManyField(User, related_name='liked_messages')

class Player(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=1)
    currency = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    side = models.CharField(max_length=10)

class Game(models.Model):
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='created_games')
    player2 = models.ForeignKey(Player, on_delete=models.SET_NULL, related_name='joined_games', null=True, blank=True)
    bet = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
