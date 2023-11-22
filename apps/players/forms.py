from django import forms
from players.models.teams import Teams

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
