"""
Base settings, extended by the dev/staging/production settings.
"""

import os
from django.utils.log import DEFAULT_LOGGING

DEBUG = False

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)
)))


MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    # 'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'widget_tweaks',
    'corsheaders',
    'django_ses',
    'apps.landing',
    'apps.base_accounts',
    'apps.accounts',
)

# Domain configuration
SITE_SCHEMA = os.environ.get('SCHEMA', 'http')
SITE_DOMAIN = os.environ.get('FQDN', 'api.radiusfinancial.com')
SITE_DOMAIN_WEB = "radiusfinancial.com"

# todo: change this
FRONTEND_OAUTH_REDIRECT = 'http://radiusfinancial.com/oauth/'

# 3rd party framework configuration
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'apps.accounts.authentication.NoCSRFSessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.AcceptHeaderVersioning',
    # 'PAGE_SIZE': 100,
}

CORS_ORIGIN_WHITELIST = [
    "radiusfinancial.com"
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', 'radius_dev'),
        'USER': os.environ.get('DB_USER', 'radius'),
        'PASSWORD': os.environ.get('DB_PASS', 'radius'),
        'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Auth Configuration
AUTH_USER_MODEL = 'accounts.EmailUser'
LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'

#############################################################################
# You will only rarely need to change anything below here.
#############################################################################


class EmailSettings:
    HEADER_COLOR = "#03a9f4"  # Material Blue 500
    BG_COLOR = "#f5f5f5"  # Material Grey 100
    CONTENT_COLOR = "#ffffff"  # White
    HIGHLIGHT_COLOR = "#f5f5f5"  # Material Grey 100
    # todo: need to change this
    LOGO_URL = "http://www.valueinvestasia.com/wp-content/uploads/2015/01/insurance-management.jpg"
    LOGO_ALT_TEXT = ""
    TERMS_URL = ""
    PRIVACY_URL = ""
    UNSUBSCRIBE_URL = ""
    FONT_CSS = 'font-family: "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;'
    FONT_CSS_HEADER = 'font-family: "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;'


EMAIL = EmailSettings()
EMAIL_BACKEND = 'django_ses.SESBackend'
DEFAULT_FROM_EMAIL = 'support@radiusfinancial.com'
# Additionally, if you are not using the default AWS region of us-east-1,
# you need to specify a region, like so:
AWS_SES_REGION_NAME = 'us-west-2'
AWS_SES_REGION_ENDPOINT = 'email.us-west-2.amazonaws.com'


# General
MANAGERS = ADMINS = (
    ('radius Admin', 'admin@radiusfinancial.com'),
)

radius = {
    'ADMIN': {
        'SITE_TITLE': "radius",
    }
}

# Host names
INTERNAL_IPS = ('127.0.0.1',)
ALLOWED_HOSTS = [SITE_DOMAIN, 'localhost']


# Logging
# The numeric values of logging levels are in the following table:
#
# CRITICAL    50
# ERROR       40
# WARNING     30
# INFO        20
# DEBUG       10
# NOTSET      0 [default]
#
# Messages which are less severe than the specified level will be ignored.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': DEFAULT_LOGGING['filters'],
    'formatters': {
        'default': {
            '()': 'logging.Formatter',
            'format': '[%(asctime)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'debug': {
            '()': 'logging.Formatter',
            'format': '[%(asctime)s] %(levelname)s - %(name)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'filters': ['require_debug_false'],
        },
        'debug-console': {
            'level': 'INFO',  # DEBUG level here is *extremely* noisy
            'class': 'logging.StreamHandler',
            'formatter': 'debug',
            'filters': ['require_debug_true'],
        },
        'file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'filename': '/var/log/radius/django.log',
            'maxBytes': 1000000,  # 1MB
            'delay': True,
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'debug-console', 'file'],
            'level': 'NOTSET',
            'propagate': False,
        },
        'django': {
            'handlers': ['console', 'debug-console', 'file'],
            'level': 'NOTSET',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console', 'debug-console', 'file'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}


# Caching
CACHES = {
    'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}
}


# Templates
from apps import base_accounts
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'radius', 'templates'),
            os.path.join(base_accounts.__path__[0], 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# password policies
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 9,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


#############################################################################
# You shouldn't ever have to change anything below here.
#############################################################################


# Static/Media
MEDIA_ROOT = '/var/media/radius/media'
MEDIA_URL = '/media/'
STATIC_ROOT = '/var/media/radius/static'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'radius', 'static'),
)

# URLs
ROOT_URLCONF = 'radius.urls'


# ./manage.py runserver WSGI configuration
WSGI_APPLICATION = 'radius.wsgi.application'


# i18n
USE_TZ = True
TIME_ZONE = 'America/Denver'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True


# Secrets
SECRET_KEY = '{{ secret_key }}'
