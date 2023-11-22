from base.models import BaseModel
from django.db import models


class Player(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="players/")
    description = models.TextField(max_length=500)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name
