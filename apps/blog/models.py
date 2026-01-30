from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import markdown


class BlogPost(models.Model):
    """Blog posts showcasing knowledge and writing."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    excerpt = models.TextField(max_length=300, help_text="Short description for previews")
    content = models.TextField(help_text="Full blog post content (supports Markdown)")
    cover_image = models.ImageField(upload_to='blog/', blank=True, null=True, help_text="Featured image")
    external_url = models.URLField(blank=True, help_text="Link to externally published blog (e.g., Medium, Dev.to)")
    platform_name = models.CharField(max_length=50, blank=True, help_text="Platform name for external link (e.g., Medium, Dev.to)")
    
    # Metadata
    author = models.CharField(max_length=100, default="Pawan Kumar")
    published_date = models.DateTimeField(help_text="When to publish this post")
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False, help_text="Make post visible")
    is_featured = models.BooleanField(default=False, help_text="Show on homepage")
    
    # SEO
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags")
    read_time = models.IntegerField(default=5, help_text="Estimated reading time in minutes")
    views = models.IntegerField(default=0, help_text="Number of views")
    order = models.IntegerField(default=0, help_text="Display order (lower first)")
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', '-published_date']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})
    
    def get_tags_list(self):
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
    
    def get_content_as_html(self):
        """Convert markdown content to HTML."""
        return markdown.markdown(
            self.content,
            extensions=['extra', 'codehilite', 'nl2br', 'sane_lists']
        )
