"""
Production settings
"""
import dj_database_url
from .base import *

DATABASES = {
    'default': dj_database_url.config(
        default=env('DATABASE_URL'),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Security settings
# TEMPORARILY ENABLE DEBUG TO SEE ERROR DETAILS
DEBUG = True  # CHANGE BACK TO False AFTER FIXING!

# Allowed hosts - ensure Render domain is included
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['portfolio-xj33.onrender.com'])

# Disable SSL redirect temporarily to debug
SECURE_SSL_REDIRECT = False  # Changed from env.bool to False for debugging
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Email backend for production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'