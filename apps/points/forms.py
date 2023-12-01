from django import forms
from points.models.matchday import MatchDay
from points.models.points import PlayerPoints
from players.models import Player,Teams
from points.models.teamresult import TeamResult

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

    matchplayed = forms.BooleanField(
        initial=True,
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    goal = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    assist = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    yellowcard = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    redcard = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )


class TeamResultCreateForm(forms.ModelForm):
    class Meta:
        model = TeamResult
        fields = ['matchday','team_a','team_b','team_a_score','team_b_score','desc']

    matchday = forms.ModelChoiceField(
        queryset=MatchDay.objects.all(),
        empty_label="Select a Match Day to store points",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    team_a = forms.ModelChoiceField(
        queryset=Teams.objects.all(),
        empty_label="Select Team A",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    team_b = forms.ModelChoiceField(
        queryset=Teams.objects.all(),
        empty_label="Select Team B",
        widget=forms.Select(attrs={'class': 'form-control'})
    )


    team_a_score = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    team_b_score = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    desc = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )