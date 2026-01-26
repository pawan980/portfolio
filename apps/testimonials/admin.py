from django.contrib import admin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'company', 'position', 'rating', 'is_featured', 'order')
    list_filter = ('is_featured', 'rating', 'created_at')
    search_fields = ('author', 'company', 'content')
    list_editable = ('is_featured', 'order')
    fieldsets = (
        ('Author Information', {
            'fields': ('author', 'position', 'company', 'photo')
        }),
        ('Testimonial', {
            'fields': ('content', 'rating')
        }),
        ('Display Options', {
            'fields': ('is_featured', 'order')
        }),
    )
