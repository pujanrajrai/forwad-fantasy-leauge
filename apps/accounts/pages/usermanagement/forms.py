from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models.profiles import Profile,GENDER_CHOICES
from accounts.models.users import User
from django.contrib.auth.forms import PasswordChangeForm

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




class UserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['old_password']  # Remove the 'Old Password' field

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password1')
        confirm_password = cleaned_data.get('new_password2')

        if new_password != confirm_password:
            raise forms.ValidationError("The new passwords do not match.")

        return cleaned_data
