"""
Models for project showcase.
"""

from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from apps.core.models import TimeStampedModel


class Project(TimeStampedModel):
    """Portfolio project model."""
    
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('planned', 'Planned'),
    ]
    
    # Basic Information
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=200)
    description = models.TextField()
    
    # Images
    thumbnail = models.ImageField(upload_to='projects/thumbnails/')
    featured_image = models.ImageField(upload_to='projects/featured/', blank=True, null=True)
    
    # Details
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed')
    technologies = models.CharField(max_length=500, help_text="Comma-separated")
    
    # Links
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    
    # Display
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    # Dates
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    
    class Meta:
        ordering = ['-is_featured', 'order', '-created_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('projects:detail', kwargs={'slug': self.slug})
    
    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]


class ProjectImage(TimeStampedModel):
    """Additional images for project gallery."""
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.project.title} - Image {self.order}"