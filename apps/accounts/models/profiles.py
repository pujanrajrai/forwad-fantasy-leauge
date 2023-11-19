from django.db import models
from django.conf import settings
from base.models import BaseModel


class Profile(BaseModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    fullname = models.CharField(
        max_length=255,
        verbose_name='Full Name'
    )
    teamname = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Team Name'
    )
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True,
        verbose_name='Profile Picture',

    )

    def __str__(self):
        return f"{self.user.email}'s Profile"

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
