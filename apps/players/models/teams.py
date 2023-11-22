from base.models import BaseModel
from django.db import models


class Teams(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    team_picture = models.ImageField(
        upload_to='team_pics/',
        blank=True,
        null=True,
        verbose_name='Team Picture',
    )

    def __str__(self):
        return self.name
