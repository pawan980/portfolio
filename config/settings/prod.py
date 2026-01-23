"""
Production settings
"""
import os
import dj_database_url
from .base import *

DATABASES = {
    'default': dj_database_url.config(
        default=env('DATABASE_URL'),
        conn_max_age=600,
        conn_health_checks=True,
        ssl_require=True,
    )
}

# Security settings
DEBUG = True
TEMPLATE_DEBUG = False 

# Allowed hosts - ensure Render domain is included
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['portfolio-xj33.onrender.com'])

# Security middleware settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', default=True)
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SAMESITE = 'Lax'
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# Static files with WhiteNoise compression
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Production logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': env('DJANGO_LOG_LEVEL', default='INFO'),
            'propagate': False,
        },
    },
}

# Email backend - console logging (contact submissions saved to database)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='noreply@portfolio-xj33.onrender.com')

# AWS S3 Settings for media files
USE_S3 = env.bool('USE_S3', default=False)  # Disabled by default

if USE_S3:
    # AWS S3 configuration
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID', default='')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY', default='')
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME', default='')
    AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME', default='us-east-1')
    
    # Only configure S3 if credentials are provided
    if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY and AWS_STORAGE_BUCKET_NAME:
        # S3 settings - keep bucket private, use querystring auth
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com'
        AWS_S3_OBJECT_PARAMETERS = {
            'CacheControl': 'max-age=86400',
        }
        AWS_DEFAULT_ACL = None  # Use bucket's default (private)
        AWS_QUERYSTRING_AUTH = True  # Generate signed URLs
        AWS_S3_FILE_OVERWRITE = False
        AWS_LOCATION = 'media'
        AWS_S3_SIGNATURE_VERSION = 's3v4'
        
        # Media files configuration
        DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
    else:
        # Fall back to local storage if S3 credentials missing
        MEDIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
else:
    # Local media files (for development)
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')