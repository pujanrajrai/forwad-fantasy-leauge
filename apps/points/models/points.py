from django.db import models
from base.models import BaseModel
from players.models import Player
from .matchday import MatchDay


class PlayerPoints(BaseModel):
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    matchday = models.ForeignKey(MatchDay, on_delete=models.PROTECT)
    matchplayed = models.BooleanField(default=True)
    goal = models.PositiveIntegerField()
    assist = models.PositiveIntegerField()
    yellowcard = models.PositiveIntegerField()
    redcard = models.PositiveIntegerField()

    def __str__(self):
        return self.player.name

    # formula hallna baki xa update ko kam pani garna baki xa
