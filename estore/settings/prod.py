from .base import *

DEBUG = False

ALLOWED_HOSTS = []


ADMINS = (
    ('admim', 'admin@email.com')
)


# DATABASE CONFIGURATIONS
DATABASES = {
    'default': {

    }
}


# EMAIL CONFIGURATION

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "brownjunior956@gmail.com"
EMAIL_HOST_PASSWORD = "tjfcbmkiuutyewti"
EMAIL_USE_TLS = True

# TODO 1: SET THE prod.py AS THE DEFAULT DJANGO SETTINGS CONF IN PRODUCTION
# TODO code: export DJANGO_SETTINGS_MODULE=estore.settings.pro
