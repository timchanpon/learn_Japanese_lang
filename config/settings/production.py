from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]


# Register static root
STATIC_ROOT = '/usr/share/nginx/html/static'


# Logging settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    # Logger setting
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        'home': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        'words': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        'accounts': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    },

    # Handler setting
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'prod',
            'when': 'D',  # Log rotation
            'interval': 1,  # Log rotation
            'backupCount': 7,  # Save 7 logs
        },
    },

    # Formatter setting
    'formatters': {
        'prod': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}


# Security settings
# security.W006
SECURE_CONTENT_TYPE_NOSNIFF = True
# security.W007
SECURE_BROWSER_XSS_FILTER = True
# security.W019
X_FRAME_OPTIONS = 'DENY'

# Security settings for SSL
# security.W004
SECURITY_HSTS_SECONDS = 31536000
SECURITY_HSTS_INCLUDE_SUBDOMAINS = True
# security.W008
SECURE_SSL_REDIRECT = True
# security.W012
SESSION_COOKIE_SECURE = True
# security.W016
CSRF_COOKIE_SECURE = True
# security.W021
SECURE_HSTS_PRELOAD = True
