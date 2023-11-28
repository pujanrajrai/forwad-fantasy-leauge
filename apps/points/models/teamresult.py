from django.db import models
from base.models import BaseModel
from players.models import Teams, Player

from .matchday import MatchDay


class TeamResult(BaseModel):
    matchday = models.ForeignKey(MatchDay, on_delete=models.PROTECT)
    team_a = models.ForeignKey(
        Teams, on_delete=models.PROTECT, related_name='teama')
    team_b = models.ForeignKey(
        Teams, on_delete=models.PROTECT, related_name='teamb')
    team_a_score = models.PositiveIntegerField()
    team_b_score = models.PositiveIntegerField()
    desc = models.TextField()

    class Meta:
        unique_together = ('matchday', 'team_a', 'team_b')

    def __str__(self):
        return f"{self.matchday.name} {self.team_a.name} vs {self.team_b.name}"
