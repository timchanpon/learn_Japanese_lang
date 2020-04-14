from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]


# Register static root
STATIC_ROOT = '/usr/share/nginx/html/static'


# Security settings
# security.W006
SECURE_CONTENT_TYPE_NOSNIFF = True
# security.W007
SECURE_BROWSER_XSS_FILTER = True
# security.W019
X_FRAME_OPTIONS = 'DENY'

# Security settings for https
# security.W004
# SECURITY_HSTS_SECONDS = 31536000
# SECURITY_HSTS_INCLUDE_SUBDOMAINS = True
# security.W008
# SECURE_SSL_REDIRECT = True
# security.W012
# SESSION_COOKIE_SECURE = True
# security.W016
# CSRF_COOKIE_SECURE = True
# security.W021
# SECURE_HSTS_PRELOAD = True
