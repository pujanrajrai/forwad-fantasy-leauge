from rest_framework_simplejwt.tokens import AccessToken
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.status import HTTP_403_FORBIDDEN
from rest_framework.response import Response
from django.contrib import auth
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import redirect
from accounts.models import User
from django.http import JsonResponse
from rest_framework import status


def has_roles(allowed_roles):
    def decorator(view_function):
        def wrap(request, *args, **kwargs):
            try:
                user = request.user
                if user.is_authenticated:
                    if not user.is_blocked:
                        if user.role in allowed_roles:
                            return view_function(request, *args, **kwargs)
                        else:
                            raise PermissionDenied
                    else:
                        auth.logout(request)
                        return HttpResponse('Your account is blocked. Please contact admin')
                else:
                    return redirect('login')
            except Exception as e:
                print(e)
                return JsonResponse({'error': 'An error occurred'}, status=status.HTTP_401_UNAUTHORIZED)
        return wrap
    return decorator
