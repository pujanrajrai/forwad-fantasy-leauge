from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models.profiles import Profile,GENDER_CHOICES
from accounts.models.users import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'role']
        # Add any additional fields or customization you need

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['fullname', 'teamname', 'gender', 'profile_picture']
        # Add any additional fields or customization you need
