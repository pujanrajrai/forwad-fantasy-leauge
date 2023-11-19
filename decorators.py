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
from accounts.models import MyUser
from django.http import JsonResponse
from rest_framework import status


def is_superadmin(view_func):
    @authentication_classes([JWTAuthentication])
    @permission_classes([IsAuthenticated])
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            # Get the user's role or None if not available
            username = request.user.username
            if username == "demouser":
                from accounts.models import Demouser
                try:
                    demouser = Demouser.objects.last()
                    demouser.demouser = True
                    demouser.save()
                except:
                    demouser = True
            else:
                from accounts.models import Demouser
                try:
                    demouser = Demouser.objects.last()
                    demouser.demouser = False
                    demouser.save()
                except:
                    demouser = True
            user_role = request.user.role

            if user_role != "superadmin":
                return Response({"error": "You don't have permission to access this resource."},
                                status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({"error": "Login is required to access this resource."},
                            status=status.HTTP_401_UNAUTHORIZED)
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def is_superadmin():
    def decorator(view_function):
        def wrap(request, *args, **kwargs):
            user = request.user
            if user.is_authenticated:
                username = request.user.username
                if username == "demouser":
                    from accounts.models import Demouser
                    try:
                        demouser = Demouser.objects.last()
                        demouser.demouser = True
                        demouser.save()
                    except:
                        demouser = True
                else:
                    from accounts.models import Demouser
                    try:
                        demouser = Demouser.objects.last()
                        demouser.demouser = False
                        demouser.save()
                    except:
                        demouser = True
                if not user.is_blocked:
                    if user.role == 'superadmin' or user.role == 'admin':
                        return view_function(request, *args, **kwargs)
                    else:
                        raise PermissionDenied
                else:
                    auth.logout(request)
                    return HttpResponse('Your account is blocked. Please contact admin')
            else:
                return redirect('login')

        return wrap
    return decorator


def has_roles(allowed_roles):
    def decorator(view_function):
        def wrap(request, *args, **kwargs):
            try:
                user = request.user
                authorization_header = request.META.get('HTTP_AUTHORIZATION')

                if authorization_header:
                    token_prefix, token = authorization_header.split()
                    if token_prefix != 'Bearer':
                        return JsonResponse({'error': 'Invalid token prefix'}, status=status.HTTP_401_UNAUTHORIZED)
                    try:
                        access_token = AccessToken(token)
                        user_id = access_token.payload['user_id']
                        user = MyUser.objects.get(pk=user_id)
                        username = user.username
                        if username == "demouser":
                            from accounts.models import Demouser
                            try:
                                demouser = Demouser.objects.last()
                                demouser.demouser = True
                                demouser.save()
                            except:
                                demouser = True
                        else:
                            from accounts.models import Demouser
                            try:
                                demouser = Demouser.objects.last()
                                demouser.demouser = False
                                demouser.save()
                            except:
                                demouser = True

                        if user.role in allowed_roles:
                            return view_function(request, *args, **kwargs)
                        else:
                            return JsonResponse({'error': 'PermissionDenied'}, status=status.HTTP_401_UNAUTHORIZED)
                    except Exception as e:
                        return JsonResponse({'error': 'Invalid or expired token'}, status=status.HTTP_401_UNAUTHORIZED)
                elif user.is_authenticated:
                    username = request.user.username
                    if username == "demouser":
                        from accounts.models import Demouser
                        try:
                            demouser = Demouser.objects.last()
                            demouser.demouser = True
                            demouser.save()
                        except:
                            demouser = True
                    else:
                        from accounts.models import Demouser
                        try:
                            demouser = Demouser.objects.last()
                            demouser.demouser = False
                            demouser.save()
                        except:
                            demouser = True
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


def api_has_roles(allowed_roles):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            try:
                # import pdb
                # pdb.set_trace()
                # user = request.user
                authorization_header = request.META.get('HTTP_AUTHORIZATION')
                if authorization_header:
                    token_prefix, token = authorization_header.split()
                    if token_prefix != 'Bearer':
                        return JsonResponse({'error': 'Invalid token prefix'}, status=status.HTTP_401_UNAUTHORIZED)
                    try:
                        access_token = AccessToken(token)
                        user_id = access_token.payload['user_id']
                        user = MyUser.objects.get(pk=user_id)
                        username = user.username
                        if username == "demouser":
                            from accounts.models import Demouser
                            try:
                                demouser = Demouser.objects.last()
                                demouser.demouser = True
                                demouser.save()
                            except:
                                demouser = True
                        if user.role in allowed_roles:
                            return view_func(request, *args, **kwargs)
                        else:
                            return JsonResponse({'error': 'PermissionDenied'}, status=status.HTTP_403_FORBIDDEN)
                    except Exception as e:
                        return JsonResponse({'error': 'Invalid or expired token e'}, status=status.HTTP_401_UNAUTHORIZED)
                else:
                    return JsonResponse({'error': 'Invalid or expired token. not autorized'}, status=status.HTTP_401_UNAUTHORIZED)
            except Exception as e:
                print(e)
                return JsonResponse({'error': 'An error occurred'}, status=status.HTTP_401_UNAUTHORIZED)

        return _wrapped_view

    return decorator
