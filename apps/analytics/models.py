"""
Analytics models for tracking user interactions.
"""
from django.db import models
from apps.core.models import TimeStampedModel


class ResumeDownload(TimeStampedModel):
    """Track resume downloads for analytics."""
    
    # Request information
    ip_address = models.GenericIPAddressField(help_text="IP address of downloader")
    user_agent = models.TextField(blank=True, help_text="Browser/device information")
    referrer = models.URLField(blank=True, max_length=500, help_text="Page they came from")
    
    # Location data (optional - can be populated via IP lookup)
    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    
    # Download context
    download_source = models.CharField(
        max_length=50,
        choices=[
            ('modal', 'Resume Modal'),
            ('direct', 'Direct Link'),
            ('navbar', 'Navbar'),
        ],
        default='modal',
        help_text="Where the download was initiated"
    )
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Resume Download'
        verbose_name_plural = 'Resume Downloads'
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['ip_address']),
        ]
    
    def __str__(self):
        return f"Download from {self.ip_address} on {self.created_at.strftime('%Y-%m-%d %H:%M')}"
    
    @classmethod
    def get_total_downloads(cls):
        """Get total number of downloads."""
        return cls.objects.count()
    
    @classmethod
    def get_unique_ips(cls):
        """Get count of unique IP addresses."""
        return cls.objects.values('ip_address').distinct().count()
    
    @classmethod
    def get_downloads_by_source(cls):
        """Get download counts grouped by source."""
        return cls.objects.values('download_source').annotate(
            count=models.Count('id')
        ).order_by('-count')
    
    @classmethod
    def get_recent_downloads(cls, limit=10):
        """Get most recent downloads."""
        return cls.objects.all()[:limit]
