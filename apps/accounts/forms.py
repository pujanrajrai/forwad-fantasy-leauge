from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models.users import User
from django.forms.widgets import Select, ClearableFileInput

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'role']

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'style': 'color:black'})
    )

    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'color:black'}),
        label='Password'
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'style': 'color:black'}),
        label='Confirm Password'
    )
