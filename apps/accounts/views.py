from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import redirect
from . forms import UserRegisterForm
# Create your views here.


def home(request):
    return render(request, 'base.html')



def login(request):
    context={}
    if request.user.is_authenticated:
        if request.user.role=='admin':
            return redirect('accounts:pages:users:user_list')
        if request.user.role=='player':
            return redirect('users:profile_redirect')
            # Redirrect to leader board
            # return redirect('accounts:pages:users:user_list')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('accounts:pages:users:user_list')
        else:
            context['errors'] = "User name or password is incorrect"
            context['username'] = username
            return render(request, 'accounts/login.html', context)
    return render(request, 'accounts/login.html',context)



def logout(request):
    auth.logout(request)
    return redirect('accounts:login')

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'User profile created successfully.')
            return redirect(reverse('accounts:login'))

    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'accounts/usermanagement/create.html', {'user_form': user_form, 'profile_form': profile_form})
