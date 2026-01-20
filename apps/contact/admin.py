from django.contrib import admin
from .models import ContactSubmission


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'ip_address', 'user_agent')
    
    def has_add_permission(self, request):
        return False