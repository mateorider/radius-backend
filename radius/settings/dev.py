"""
Development settings, extends the base settings.
"""
from .production import *

DEBUG = True
SITE_DOMAIN = "localhost:8000"  # should not have a trailing slash
SITE_DOMAIN_WEB = "localhost:9000"  # should not have a trailing slash
MEDIA_ROOT = os.path.join(BASE_DIR, 'server', 'dev', 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'server', 'dev', 'static') # The absolute path to the directory where collectstatic will collect static files for deployment.
AUTH_PASSWORD_VALIDATORS = []  # disable password policies
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# TODO: Remove Pagination for now
# REST_FRAMEWORK['PAGE_SIZE'] = 1

CORS_ORIGIN_ALLOW_ALL = True

# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'gmail'
# EMAIL_HOST_PASSWORD = 'gmailcode'
# EMAIL_PORT = 587
