from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Experience


@admin.register(Experience)
class ExperienceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('position', 'company_name', 'employment_type', 'start_date', 'is_current', 'is_visible', 'order')
    list_filter = ('employment_type', 'is_current', 'is_visible')
    list_editable = ('is_current', 'is_visible')
    search_fields = ('position', 'company_name', 'description')
    
    fieldsets = (
        ('Company', {
            'fields': ('company_name', 'company_logo', 'company_url', 'location')
        }),
        ('Position', {
            'fields': ('position', 'employment_type', 'description', 'technologies')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        ('Display', {
            'fields': ('is_visible', 'order')
        }),
    )