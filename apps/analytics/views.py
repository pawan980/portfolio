"""
Views for analytics tracking.
"""
from django.http import FileResponse, Http404
from django.views import View
from django.conf import settings
from .models import ResumeDownload
from apps.core.models import SiteSettings


def get_client_ip(request):
    """Get client IP address from request."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class ResumeDownloadView(View):
    """Handle resume downloads with analytics tracking."""
    
    def get(self, request):
        """Serve resume file and track download."""
        try:
            site = SiteSettings.objects.first()
            if not site or not site.resume_file:
                raise Http404("Resume not found")
            
            # Track the download
            ResumeDownload.objects.create(
                ip_address=get_client_ip(request),
                user_agent=request.META.get('HTTP_USER_AGENT', ''),
                referrer=request.META.get('HTTP_REFERER', ''),
                download_source=request.GET.get('source', 'direct')
            )
            
            # Serve the file
            response = FileResponse(
                site.resume_file.open('rb'),
                content_type='application/pdf'
            )
            response['Content-Disposition'] = f'attachment; filename="{site.full_name}_Resume.pdf"'
            
            return response
            
        except Exception as e:
            raise Http404(f"Error serving resume: {str(e)}")
