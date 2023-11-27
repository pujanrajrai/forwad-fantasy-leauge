from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import redirect
# Create your views here.


def home(request):
    return render(request, 'base.html')



def login(request):
    context={}
    if request.user.is_authenticated:
        if request.user:
            return redirect('accounts:pages:users:user_list')
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

