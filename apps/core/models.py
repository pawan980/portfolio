"""
Core models for portfolio application.
"""

from django.db import models
from django.core.validators import URLValidator


class TimeStampedModel(models.Model):
    """
    Abstract base model that provides created_at and updated_at fields.
    All models inherit this to avoid repeating timestamp fields.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class SiteSettings(TimeStampedModel):
    """
    Singleton model for site-wide settings.
    Only one instance should exist.
    """
    # Personal Information
    full_name = models.CharField(max_length=100, default="Your Name")
    tagline = models.CharField(max_length=200, default="Full Stack Developer")
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    
    # Contact Information
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    
    # Social Media
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    
    # Resume
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True)
    
    # Content Sections (Currently section only)
    current_projects = models.TextField(blank=True, help_text="Currently - Current Projects subsection")
    currently_learning = models.TextField(blank=True, help_text="Currently - Learning subsection")
    
    # Stats/Achievements
    years_experience = models.IntegerField(default=0, help_text="Years of professional experience")
    projects_completed = models.IntegerField(default=0, help_text="Number of projects completed")
    clients_served = models.IntegerField(default=0, help_text="Number of clients served")
    certifications = models.IntegerField(default=0, help_text="Number of certifications obtained")
    
    # SEO
    meta_description = models.CharField(max_length=160, blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)
    
    # Features
    enable_dark_mode = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
    
    def __str__(self):
        return f"Site Settings - {self.full_name}"
    
    def save(self, *args, **kwargs):
        """Ensure only one instance exists (singleton pattern)."""
        self.pk = 1
        super().save(*args, **kwargs)
    
    @classmethod
    def load(cls):
        """Load the singleton instance."""
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Skill(TimeStampedModel):
    """Technical skills with categories and proficiency levels."""
    
    CATEGORY_CHOICES = [
        ('programming', 'Programming Languages'),
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('devops', 'DevOps & Tools'),
        ('cloud', 'Cloud Platforms'),
        ('other', 'Other'),
    ]
    
    PROFICIENCY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]
    
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    proficiency = models.CharField(max_length=20, choices=PROFICIENCY_CHOICES, default='intermediate')
    icon = models.CharField(max_length=50, blank=True, help_text="Icon class (e.g., devicon-python-plain)")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['category', 'order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"