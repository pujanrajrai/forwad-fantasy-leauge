from base.models import BaseModel
from django.db import models
from .teams import Teams

class Player(BaseModel):
    team = models.ForeignKey(
        Teams, on_delete=models.PROTECT,null=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="players/")
    description = models.TextField(max_length=500)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name
