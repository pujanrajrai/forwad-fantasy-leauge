""" 
#todo
CRUD of user including password change and blocking user
"""
from django.shortcuts import redirect, render
from .forms import ProfileForm, UserForm
from django.contrib import messages
from accounts.models.users import User

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
    model = User
    template_name = 'accounts/usermanagement/list.html'
    context_object_name = 'user_list'  # Specify the variable name in the template

    def get_queryset(self):
        # Customize the queryset if needed
        return User.objects.all()
