from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']


# DATABASE CONFIGURATION
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

# STATIC FILES CONFIGURATION
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]


# EMAIL_CONFIGURATION
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
MAILER_EMAIL_BACKEND = EMAIL_BACKEND
EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = None
EMAIL_HOST_USER = None
EMAIL_PORT = 1025
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

"""
IN DEVELOPMENT MODE, RUN
export DJANGO_SETTINGS_MODULE=estore.settings.dev
"""