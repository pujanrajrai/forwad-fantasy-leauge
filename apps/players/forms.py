from django import forms
from players.models.teams import Teams
from players.models.players import Player

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