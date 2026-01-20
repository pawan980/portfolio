from django.contrib import admin
from .models import SiteSettings, Skill


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'tagline', 'bio', 'profile_image')
        }),
        ('Contact', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Social Media', {
            'fields': ('github_url', 'linkedin_url', 'twitter_url')
        }),
        ('Resume', {
            'fields': ('resume_file',)
        }),
        ('SEO', {
            'fields': ('meta_description', 'meta_keywords')
        }),
    )
    
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'order', 'is_active')
    list_filter = ('category', 'proficiency', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name',)