"""
Context processors for making data available across all templates.
"""

from django.db import connection
from .models import SiteSettings


def site_data(request):
    """Add site settings to all template contexts."""
    try:
        # Check if the table exists using Django introspection
        table_names = connection.introspection.table_names()
        if 'core_sitesettings' in table_names:
            return {
                'site': SiteSettings.load(),
            }
        else:
            return {
                'site': None,
            }
    except Exception:
        # If anything fails, return None
        return {
            'site': None,
        }