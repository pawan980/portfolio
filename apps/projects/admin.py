from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from .models import Project, ProjectImage


class ProjectImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ('image', 'caption', 'order')


@admin.register(Project)
class ProjectAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'status', 'is_featured', 'is_published', 'order', 'created_at')
    list_filter = ('status', 'is_featured', 'is_published')
    list_editable = ('is_featured', 'is_published')
    search_fields = ('title', 'description', 'technologies')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]
    
    fieldsets = (
        ('Basic', {
            'fields': ('title', 'slug', 'short_description', 'description')
        }),
        ('Images', {
            'fields': ('thumbnail', 'featured_image')
        }),
        ('Details', {
            'fields': ('status', 'technologies', 'github_url', 'live_url')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date')
        }),
        ('Display', {
            'fields': ('is_featured', 'is_published', 'order')
        }),
    )