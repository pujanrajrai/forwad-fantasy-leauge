from django.shortcuts import render
from django.shortcuts import redirect, render,get_object_or_404
from accounts.pages.usermanagement.forms import ProfileForm, UserForm,UserPasswordChangeForm
from django.contrib import messages
from accounts.models.users import User
from accounts.models.profiles import Profile
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
from django.views.generic import ListView
from django.urls import reverse
from django.views.generic.edit import CreateView
from players.models.userteam import UserSelection
from . forms import UserTeamCreateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView


# Create your views here.
class UserProfileRedirectView(View):
    template_name = 'users/userprofile/user_profile.html'  # Change this to the actual template name for the user profile page
    
    def get(self, request):
        user_id=request.user.id
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


class UserTeamCreateView(CreateView):
    model = UserSelection
    form_class = UserTeamCreateForm
    template_name = 'players/userteam/create.html'
    success_url = reverse_lazy('users:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class UserTeamListView(LoginRequiredMixin, ListView):
    model = UserSelection
    template_name = 'users/userteam/list.html'
    context_object_name = 'userteam_list'

    def get_queryset(self):
        # Filter the queryset to show only teams of the logged-in user
        return UserSelection.objects.filter(user=self.request.user)

class UserTeamUpdateView(UpdateView):
    model = UserSelection
    form_class = UserTeamCreateForm  # Use the same form as in your CreateView
    template_name = 'users/userteam/update.html'  # Update with your actual template name
    success_url = reverse_lazy('users:list')  # Update with your actual success URL

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs