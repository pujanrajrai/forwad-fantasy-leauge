from django import forms
from points.models.matchday import MatchDay
from points.models.points import PlayerPoints
from players.models import Player


class MatchDayCreateForm(forms.ModelForm):
    class Meta:
        model = MatchDay
        fields = ['name']

    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'color: black'}),
        label='Match Day'
    )

class PlayerPointsCreateForm(forms.ModelForm):
    class Meta:
        model = PlayerPoints
        fields = ['player','matchday','matchplayed','goal','assist','yellowcard','redcard']

    player = forms.ModelChoiceField(
        queryset=Player.objects.all(),
        empty_label="Select a player to store points",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    matchday = forms.ModelChoiceField(
        queryset=MatchDay.objects.all(),
        empty_label="Select a Match Day to store points",
        widget=forms.Select(attrs={'class': 'form-control'})
    )


