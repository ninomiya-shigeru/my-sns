# SECURITY WARNING: don't run with debug turned on in production!
from .settings_common import *

DEBUG = True

ALLOWED_HOSTS = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

