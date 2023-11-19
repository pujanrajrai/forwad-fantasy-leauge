"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from decouple import config

from django.core.wsgi import get_wsgi_application

settings_key = config('settings_key', default='core.settings.local')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_key)

application = get_wsgi_application()
