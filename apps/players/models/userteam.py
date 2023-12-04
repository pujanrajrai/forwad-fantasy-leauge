from django.db import models
from accounts.models import User
from .players import Player


class UserSelection(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    player1 = models.ForeignKey(
        Player, related_name='player1', on_delete=models.CASCADE)
    player2 = models.ForeignKey(
        Player, related_name='player2', on_delete=models.CASCADE)
    player3 = models.ForeignKey(
        Player, related_name='player3', on_delete=models.CASCADE)
    player4 = models.ForeignKey(
        Player, related_name='player4', on_delete=models.CASCADE)
    player5 = models.ForeignKey(
        Player, related_name='player5', on_delete=models.CASCADE)

    class Meta:
        # Add a unique constraint to ensure each user has a unique selection
        constraints = [
            models.UniqueConstraint(fields=[
                                    'user', 'player1', 'player2', 'player3', 'player4', 'player5'], name='unique_user_selection')
        ]

    def __str__(self):
        return f"{self.user}'s Selection"

    def save(self, *args, **kwargs):
        # Check if all five players are unique within the selection
        players = [self.player1, self.player2,
                   self.player3, self.player4, self.player5]
        if len(set(players)) != len(players):
            raise ValueError("Each player in the selection must be unique.")

        super().save(*args, **kwargs)
