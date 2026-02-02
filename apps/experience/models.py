"""
Models for work experience.
"""

from django.db import models
from apps.core.models import TimeStampedModel


class Experience(TimeStampedModel):
    """Work experience model."""
    
    EMPLOYMENT_TYPE_CHOICES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract'),
        ('freelance', 'Freelance'),
        ('internship', 'Internship'),
    ]
    
    # Company
    company_name = models.CharField(max_length=200)
    company_logo = models.ImageField(upload_to='experience/logos/', blank=True, null=True)
    company_url = models.URLField(blank=True)
    location = models.CharField(max_length=200)
    
    # Position
    position = models.CharField(max_length=200)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES, default='full_time')
    description = models.TextField()
    technologies = models.CharField(max_length=500, blank=True)
    
    # Dates
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    
    # Display
    is_visible = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', '-start_date']
    
    def __str__(self):
        return f"{self.position} at {self.company_name}"
    
    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]
    
    def get_description_as_html(self):
        """Convert description with bullet points to HTML."""
        lines = self.description.strip().split('\n')
        html_parts = []
        in_list = False
        
        for line in lines:
            line = line.strip()
            if not line:
                if in_list:
                    html_parts.append('</ul>')
                    in_list = False
                continue
            
            # Check if line starts with bullet point marker
            if line.startswith('* ') or line.startswith('- '):
                if not in_list:
                    html_parts.append('<ul class="list-disc list-inside space-y-2 text-gray-300">')
                    in_list = True
                html_parts.append(f'<li>{line[2:]}</li>')
            else:
                if in_list:
                    html_parts.append('</ul>')
                    in_list = False
                html_parts.append(f'<p>{line}</p>')
        
        if in_list:
            html_parts.append('</ul>')
        
        return ''.join(html_parts)