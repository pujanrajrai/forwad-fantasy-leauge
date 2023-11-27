from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'base.html')



def login(request):
    if request.user.is_authenticated:
        if request.user:
            return redirect('accounts:home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not form.is_valid():
            context['username'] = username
            return render(request, 'accounts/login.html', context)

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('accounts:home')
        else:
            context['errors'] = "User name or password is incorrect"
            context['username'] = username
            return render(request, 'accounts/login.html', context)
    return render(request, 'accounts/login.html')

