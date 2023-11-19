""" 
#todo
CRUD of user including password change and blocking user
"""
from django.shortcuts import redirect, render


def list(request):
    return render(request, 'accounts/usermanagement/list.html')
