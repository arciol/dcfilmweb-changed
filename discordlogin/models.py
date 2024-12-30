from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class DiscordUser(models.Model):
    user_id = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="discorduser"
    )
    discord_username = models.CharField(max_length=255)
    discord_id = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.discord_username
