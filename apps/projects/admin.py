from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from .models import Project, ProjectImage
from .forms import ProjectAdminForm


class ProjectImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ('image', 'caption', 'order')


@admin.register(Project)
class ProjectAdmin(SortableAdminMixin, admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ('title', 'get_categories_short', 'status', 'stars', 'show_on_about_page', 'order', 'created_at')
    list_filter = ('status', 'show_on_about_page')
    list_editable = ('show_on_about_page',)
    search_fields = ('title', 'description', 'technologies')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]
    
    def get_categories_short(self, obj):
        """Display categories in list view."""
        cats = obj.get_categories_display()
        if not cats:
            return '-'
        return ', '.join(cats) if len(cats) <= 2 else f"{', '.join(cats[:2])}..."
    get_categories_short.short_description = 'Categories'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'categories', 'short_description', 'description'),
            'description': 'Required fields: Title, Short Description, Description. Categories: Select one or more from the checkboxes.'
        }),
        ('Project Metadata', {
            'fields': ('project_type', 'your_role', 'team_size'),
            'description': 'Additional context about the project'
        }),
        ('Rich Documentation (Supports Markdown)', {
            'fields': ('problem_statement', 'solution_overview', 'key_features', 
                       'architecture', 'challenges', 'results_impact'),
            'classes': ('collapse',),
            'description': 'Detailed internal documentation. Use Markdown for formatting: **bold**, *italic*, `code`, - lists'
        }),
        ('Images', {
            'fields': ('thumbnail', 'featured_image'),
            'description': 'Thumbnail is required. Featured image is optional.'
        }),
        ('Details', {
            'fields': ('status', 'technologies', 'stars'),
            'description': 'Technologies field is required (comma-separated list)'
        }),
        ('Links (All Optional)', {
            'fields': ('github_url', 'live_url', 'case_study_url', 'documentation_url'),
            'classes': ('collapse',)
        }),
        ('Dates (Optional)', {
            'fields': ('start_date', 'end_date'),
            'classes': ('collapse',)
        }),
        ('Display Settings', {
            'fields': ('show_on_about_page', 'order')
        }),
    )