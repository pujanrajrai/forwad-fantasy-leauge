from datetime import timedelta
from .base import *
from decouple import config
import pymysql


SECRET_KEY = 'django-insecure-zylq^by#n!3bsq++wdxpde#lqbi_7s#w6u8bjen(*7+^khf@y^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
pymysql.install_as_MySQLdb()


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

d_name = config('d_name', default='fantasy')
d_user = config('d_user', default='root')
d_password = config('d_password', default='notpassword')
d_host = config('d_host', default='localhost')
d_port = config('d_port', default='')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': d_name,  # change this
        'USER': d_user,  # change this
        'PASSWORD': d_password,  # change this
        'HOST': d_host,
        'PORT': d_port,
        'CHARSET': 'utf8',
        'COLLATION': 'utf8_general_ci',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
APPEND_SLASH = True


# Import necessary modules
# Configure JWT token settings
SIMPLE_JWT = {
    # Access token expires after 5 minutes
    'ACCESS_TOKEN_LIFETIME': timedelta(days=7),
    # Refresh token is valid for 1 day
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=7),
}
