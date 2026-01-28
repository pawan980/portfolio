from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import SiteSettings, Skill


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'tagline', 'home_bio', 'bio', 'profile_image')
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
        ('Content Sections', {
            'fields': ('current_projects', 'currently_learning'),
            'description': 'Editable fields for Currently section on About page'
        }),
        ('Stats & Achievements', {
            'fields': ('years_experience', 'projects_completed', 'clients_served', 'certifications'),
            'description': 'Key metrics displayed on homepage'
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
class SkillAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'category', 'subcategory', 'details', 'order', 'is_active')
    list_filter = ('category', 'subcategory', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('name', 'subcategory', 'details')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'subcategory', 'details')
        }),
        ('Display', {
            'fields': ('icon', 'order', 'is_active')
        }),
    )