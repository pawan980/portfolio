"""
Context processors for making data available across all templates.
"""

from .models import SiteSettings


def site_data(request):
    """Add site settings to all template contexts."""
    return {
        'site': SiteSettings.load(),
    }