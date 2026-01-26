"""
Admin interface for analytics.
"""
from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html
from .models import ResumeDownload


@admin.register(ResumeDownload)
class ResumeDownloadAdmin(admin.ModelAdmin):
    """Admin interface for resume downloads."""
    
    list_display = ['created_at', 'ip_address', 'download_source', 'country', 'city', 'user_agent_short']
    list_filter = ['download_source', 'created_at', 'country']
    search_fields = ['ip_address', 'user_agent', 'country', 'city']
    readonly_fields = ['created_at', 'updated_at', 'ip_address', 'user_agent', 'referrer', 'country', 'city', 'download_source']
    date_hierarchy = 'created_at'
    
    def user_agent_short(self, obj):
        """Show shortened user agent."""
        if obj.user_agent:
            return obj.user_agent[:50] + '...' if len(obj.user_agent) > 50 else obj.user_agent
        return '-'
    user_agent_short.short_description = 'User Agent'
    
    def has_add_permission(self, request):
        """Disable manual addition."""
        return False
    
    def has_change_permission(self, request, obj=None):
        """Make read-only."""
        return False
    
    def changelist_view(self, request, extra_context=None):
        """Add analytics summary to list view."""
        extra_context = extra_context or {}
        
        # Get analytics data
        total_downloads = ResumeDownload.get_total_downloads()
        unique_ips = ResumeDownload.get_unique_ips()
        by_source = ResumeDownload.get_downloads_by_source()
        
        extra_context['total_downloads'] = total_downloads
        extra_context['unique_ips'] = unique_ips
        extra_context['downloads_by_source'] = by_source
        
        return super().changelist_view(request, extra_context)
