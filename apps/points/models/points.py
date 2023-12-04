from players.models import UserSelection
from django.db.models import Q
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from base.models import BaseModel
from players.models import Player
from .matchday import MatchDay
from accounts.models import Profile


class PlayerPoints(BaseModel):
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    matchday = models.ForeignKey(MatchDay, on_delete=models.PROTECT)
    matchplayed = models.BooleanField(default=True)
    goal = models.PositiveIntegerField()
    assist = models.PositiveIntegerField()
    yellowcard = models.PositiveIntegerField()
    redcard = models.PositiveIntegerField()

    class Meta:
        unique_together = ['player', 'matchday']

    def calculate_total_points(self):
        total_points = 0
        if self.matchplayed:
            total_points += 1
            total_points += self.goal * 3
            total_points += self.assist * 2
            total_points += self.yellowcard * (-1)
            total_points += self.redcard * (-3)
        return total_points

    def __str__(self):
        return self.player.name

 


@receiver(post_save, sender=PlayerPoints)
def update_user_profiles(sender, instance, **kwargs):
    # Get all UserSelection instances that include the current player
    user_selections = user_selections = UserSelection.objects.filter(
        Q(player1=instance.player) |
        Q(player2=instance.player) |
        Q(player3=instance.player) |
        Q(player4=instance.player) |
        Q(player5=instance.player)
    )
    
    # Update user profiles with the calculated points
    for user_selection in user_selections:
        user = user_selection.user
        try:
            profile = Profile.objects.get(user=user)
            profile.total_points += instance.calculate_total_points()
            profile.save()
        except Exception as e:
            print(e)
            pass
