from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'is_published', 'is_featured', 'views')
    list_filter = ('is_published', 'is_featured', 'published_date', 'created_at')
    search_fields = ('title', 'excerpt', 'content', 'tags')
    list_editable = ('is_published', 'is_featured')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'excerpt', 'content', 'cover_image')
        }),
        ('Metadata', {
            'fields': ('author', 'published_date', 'tags', 'read_time')
        }),
        ('Publishing', {
            'fields': ('is_published', 'is_featured')
        }),
        ('Stats', {
            'fields': ('views',),
            'classes': ('collapse',)
        }),
    )
