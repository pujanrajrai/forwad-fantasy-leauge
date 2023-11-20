""" 
#todo
CRUD of user including password change and blocking user
"""
from django.shortcuts import redirect, render,get_object_or_404
from .forms import ProfileForm, UserForm,UserPasswordChangeForm
from django.contrib import messages
from accounts.models.users import User
from accounts.models.profiles import Profile
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash

def create(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'User profile created successfully.')
            return redirect(reverse('accounts:pages:users:user_list'))

    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'accounts/usermanagement/create.html', {'user_form': user_form, 'profile_form': profile_form})


from django.views.generic import ListView


class UserListView(ListView):
    model = Profile
    template_name = 'accounts/usermanagement/list.html'
    context_object_name = 'user_list'  # Specify the variable name in the template

    def get_queryset(self):
        # Customize the queryset if needed
        return Profile.objects.all()


# views.py


class BlockUserView(View):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        user.is_blocked = True
        user.save()
        messages.success(request, f'User {user.email} is blocked successfully.')
        return redirect('accounts:pages:users:user_list')  # Redirect to the user list page

class UnblockUserView(View):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        user.is_blocked = False
        user.save()
        messages.success(request, f'User {user.email} is unblocked successfully.')
        return redirect('accounts:pages:users:user_list')  # Redirect to the user list page





class UserProfileRedirectView(View):
    template_name = 'accounts/usermanagement/user_profile.html'  # Change this to the actual template name for the user profile page

    def get(self, request, user_id):
        user_profile = get_object_or_404(Profile, id=user_id)
        update_form = ProfileForm(instance=user_profile)
        password_change_form = UserPasswordChangeForm(user=request.user)
        return render(request, self.template_name, {'user_profile': user_profile,'update_form': update_form,'password_change_form': password_change_form})

    def post(self, request, user_id):
        user_profile = get_object_or_404(Profile, id=user_id)
        update_form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        password_change_form = UserPasswordChangeForm(user=request.user, data=request.POST)

        if update_form.is_valid():
            update_form.save()
            messages.success(request, 'Profile updated successfully.')
        else:
            messages.error(request, 'Error updating profile. Please check the form.')

        if password_change_form.is_valid():
            user = password_change_form.save()
            # update_session_auth_hash(request, user)  # Important for maintaining user login sessions
            messages.success(request, 'Password changed successfully.')
        else:
            messages.error(request, 'Error changing password. Please check the form.')

        return redirect('accounts:pages:users:profile_redirect', user_id=user_id)

