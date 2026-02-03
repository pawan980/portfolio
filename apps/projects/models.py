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
    
    CATEGORY_CHOICES = [
        ('all_projects', 'All Projects'),
        ('web_apps', 'Web Apps'),
        ('backend', 'Backend'),
        ('ai_agents', 'AI Agents & Agentic Workflow'),
        ('open_source', 'Open Source'),
        ('data_engineering', 'Data Engineering'),
    ]
    
    # Basic Information
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=200)
    description = models.TextField()
    categories = models.CharField(max_length=200, help_text="Comma-separated category keys (e.g., 'web_apps,backend')", blank=True)
    
    # Images
    thumbnail = models.ImageField(upload_to='projects/thumbnails/')
    featured_image = models.ImageField(upload_to='projects/featured/', blank=True, null=True)
    
    # Details
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed')
    technologies = models.CharField(max_length=500, help_text="Comma-separated")
    
    # Rich Documentation Fields (Internal - Markdown supported)
    problem_statement = models.TextField(
        blank=True,
        help_text="What problem does this project solve? Why was it needed?"
    )
    solution_overview = models.TextField(
        blank=True,
        help_text="Your approach and solution. How did you solve it?"
    )
    key_features = models.TextField(
        blank=True,
        help_text="Markdown list of key features (use - for bullets)"
    )
    architecture = models.TextField(
        blank=True,
        help_text="Technical architecture, system design, implementation details"
    )
    challenges = models.TextField(
        blank=True,
        help_text="Problems you encountered and how you solved them"
    )
    results_impact = models.TextField(
        blank=True,
        help_text="Outcomes, metrics, impact, or achievements"
    )
    
    # Project Metadata
    PROJECT_TYPE_CHOICES = [
        ('personal', 'Personal Project'),
        ('freelance', 'Freelance/Client Work'),
        ('company', 'Company Project'),
        ('open_source', 'Open Source Contribution'),
        ('hackathon', 'Hackathon'),
        ('academic', 'Academic/Research'),
    ]
    project_type = models.CharField(
        max_length=50,
        blank=True,
        choices=PROJECT_TYPE_CHOICES,
        help_text="Type of project"
    )
    your_role = models.CharField(
        max_length=200,
        blank=True,
        help_text="Your role in the project (e.g., 'Full-Stack Developer', 'Team Lead')"
    )
    team_size = models.IntegerField(
        blank=True,
        null=True,
        help_text="Number of people on the team (leave blank for solo)"
    )
    
    # Links
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    case_study_url = models.URLField(blank=True, help_text="Link to detailed case study or blog post")
    documentation_url = models.URLField(blank=True, help_text="Link to project documentation")
    
    # Display
    show_on_about_page = models.BooleanField(
        default=False,
        help_text="Show this project in the Projects section of the About Me page"
    )
    order = models.IntegerField(default=0)
    stars = models.IntegerField(default=0, help_text="GitHub stars or popularity indicator")
    
    # Dates
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    
    class Meta:
        ordering = ['order', '-created_at']
    
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
    
    def get_categories_list(self):
        """Return list of category keys."""
        if not self.categories:
            return []
        return [cat.strip() for cat in self.categories.split(',') if cat.strip()]
    
    def get_categories_display(self):
        """Return list of category display names."""
        cat_dict = dict(self.CATEGORY_CHOICES)
        return [cat_dict.get(cat, cat) for cat in self.get_categories_list()]


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