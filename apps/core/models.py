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
    home_bio = models.TextField(help_text="Short bio for home page hero section", blank=True)
    bio = models.TextField(help_text="Detailed bio for about page")
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
    """Technical skills with hierarchical categories and subcategories."""
    
    CATEGORY_CHOICES = [
        ('compute', 'Compute & Application Logic'),
        ('data', 'Data Strategy & Persistence'),
        ('platform', 'Platform Engineering (Infrastructure)'),
        ('devops', 'DevOps & Delivery Automation'),
        ('observability', 'Observability & Reliability (SRE)'),
        ('architecture', 'System Architecture & Networking'),
    ]
    
    CATEGORY_DESCRIPTIONS = {
        'compute': 'Writing and structuring the code itself',
        'data': 'How data is stored, retrieved, and moved',
        'platform': 'The environment where the code runs',
        'devops': 'The pipeline that moves code to production',
        'observability': 'Keeping the system healthy and debugging production',
        'architecture': 'The high-level design and communication protocols',
    }
    
    CATEGORY_ICONS = {
        'compute': '🔧',
        'data': '💾',
        'platform': '☁️',
        'devops': '🚀',
        'observability': '📊',
        'architecture': '🏗️',
    }
    
    name = models.CharField(max_length=100, help_text="Technology name (e.g., PostgreSQL, Docker)")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, help_text="Main category")
    subcategory = models.CharField(max_length=100, help_text="Subcategory (e.g., Languages, Web Frameworks)")
    details = models.CharField(max_length=200, blank=True, help_text="Optional details (e.g., Optimization, Schema Design)")
    icon = models.CharField(max_length=100, blank=True, help_text="Devicon class (e.g., devicon-python-plain colored)")
    order = models.IntegerField(default=0, help_text="Display order within subcategory")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
    
    def __str__(self):
        if self.details:
            return f"{self.name} ({self.details}) - {self.get_category_display()}"
        return f"{self.name} - {self.get_category_display()}"
    
    def get_category_description(self):
        """Get the description for this skill's category."""
        return self.CATEGORY_DESCRIPTIONS.get(self.category, '')
    
    def get_category_icon(self):
        """Get the icon for this skill's category."""
        return self.CATEGORY_ICONS.get(self.category, '')