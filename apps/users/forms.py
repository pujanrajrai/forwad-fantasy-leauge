from django import forms
from players.models import UserSelection, Player, User
from django import forms
from players.models.teams import Teams
from players.models.players import Player
from players.models.userteam import UserSelection
from accounts.models import User



class UserTeamCreateForm(forms.ModelForm):
    class Meta:
        model = UserSelection
        fields = ['player1', 'player2', 'player3', 'player4', 'player5']

    player1 = forms.ModelChoiceField(
        queryset=Player.objects.all(),
        empty_label="Select a player for your team",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    player2 = forms.ModelChoiceField(
        queryset=Player.objects.all(),
        empty_label="Select a player for your team",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    player3 = forms.ModelChoiceField(
        queryset=Player.objects.all(),
        empty_label="Select a player for your team",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    player4 = forms.ModelChoiceField(
        queryset=Player.objects.all(),
        empty_label="Select a player for your team",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    player5 = forms.ModelChoiceField(
        queryset=Player.objects.all(),
        empty_label="Select a player for your team",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user_id = self.user.id  # Set user_id based on request.user.id
        if commit:
            instance.save()
        return instance

    def clean(self):
        cleaned_data = super().clean()

        players = [
            cleaned_data.get('player1'),
            cleaned_data.get('player2'),
            cleaned_data.get('player3'),
            cleaned_data.get('player4'),
            cleaned_data.get('player5'),
        ]

        # Check if all five players are unique within the selection
        if len(set(players)) != len(players):
            raise forms.ValidationError("Each player in the selection must be unique.")

        return cleaned_data


