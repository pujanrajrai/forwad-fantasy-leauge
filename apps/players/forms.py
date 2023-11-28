from django import forms
from players.models.teams import Teams
from players.models.players import Player
from players.models.userteam import UserSelection
from accounts.models import User

class TeamCreateForm(forms.ModelForm):
    class Meta:
        model = Teams
        fields = ['name', 'description', 'team_picture']

    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'color: black'}),
        label='Team Name'
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'color: black'}),
        label='Description'
    )

    team_picture = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        label='Team Picture',
        required=False
    )


class PlayerCreateForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['team', 'name', 'image', 'description', 'price']

    team = forms.ModelChoiceField(
        queryset=Teams.objects.all(),
        empty_label="Select a Team",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        required=False
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    price = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class UserTeamCreateForm(forms.ModelForm):
    class Meta:
        model = UserSelection
        fields = ['user', 'player1', 'player2', 'player3', 'player4','player5']

    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        empty_label="Select a User to create a team",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

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
 