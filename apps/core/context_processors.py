"""
Context processors for making data available across all templates.
"""

from django.db import connection
from .models import SiteSettings


def site_data(request):
    """Add site settings to all template contexts."""
    try:
        # Check if the table exists
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1 FROM core_sitesettings LIMIT 1")
        return {
            'site': SiteSettings.load(),
        }
    except Exception:
        # If table doesn't exist yet, return empty dict
        return {
            'site': None,
        }