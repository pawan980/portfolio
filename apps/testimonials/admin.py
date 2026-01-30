from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('author', 'company', 'position', 'rating', 'is_approved', 'is_featured', 'order')
    list_filter = ('is_approved', 'is_featured', 'rating', 'created_at')
    search_fields = ('author', 'company', 'content')
    list_editable = ('is_approved', 'is_featured')
    fieldsets = (
        ('Author Information', {
            'fields': ('author', 'position', 'company', 'photo', 'linkedin_url')
        }),
        ('Testimonial', {
            'fields': ('content', 'rating')
        }),
        ('Display Options', {
            'fields': ('is_approved', 'is_featured', 'order')
        }),
    )
