from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models.profiles import Profile,GENDER_CHOICES
from accounts.models.users import User
from django.contrib.auth.forms import PasswordChangeForm
from django.forms.widgets import Select, ClearableFileInput

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'role']
        widgets = {
            'email': forms.EmailField(attrs={'class': 'form-control', 'style': 'color:black'}),
            'role': Select(attrs={'class': 'form-control', 'style': 'color: black'}),
        }
        # Add any additional fields or customization you need

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['fullname', 'teamname', 'gender', 'profile_picture']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'style': 'color:black'}),
            'teamname': forms.TextInput(attrs={'class': 'form-control', 'style': 'color:black'}),
            'gender': Select(attrs={'class': 'form-control', 'style': 'color: black'}),
            'profile_picture': ClearableFileInput(attrs={'class': 'form-control-file'}),
            

        }




class UserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['old_password']  # Remove the 'Old Password' field
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'style': 'color: black'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'style': 'color: black'})

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password1')
        confirm_password = cleaned_data.get('new_password2')

        if new_password != confirm_password:
            raise forms.ValidationError("The new passwords do not match.")

        return cleaned_data

