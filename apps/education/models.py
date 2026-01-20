"""
Models for education and certifications.
"""

from django.db import models
from apps.core.models import TimeStampedModel


class Education(TimeStampedModel):
    """Educational background model."""
    
    DEGREE_CHOICES = [
        ('phd', 'Ph.D.'),
        ('masters', 'Master\'s Degree'),
        ('bachelors', 'Bachelor\'s Degree'),
        ('associate', 'Associate Degree'),
        ('diploma', 'Diploma'),
        ('certificate', 'Certificate'),
        ('other', 'Other'),
    ]
    
    # Institution
    institution = models.CharField(max_length=200)
    institution_logo = models.ImageField(upload_to='education/logos/', blank=True, null=True)
    institution_url = models.URLField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    
    # Degree
    degree = models.CharField(max_length=20, choices=DEGREE_CHOICES)
    field_of_study = models.CharField(max_length=200)
    grade = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    
    # Dates
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    
    # Display
    is_visible = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-start_date', 'order']
        verbose_name_plural = "Education"
    
    def __str__(self):
        return f"{self.get_degree_display()} in {self.field_of_study} - {self.institution}"


class Certification(TimeStampedModel):
    """Professional certifications."""
    
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    organization_logo = models.ImageField(upload_to='certifications/logos/', blank=True, null=True)
    
    credential_id = models.CharField(max_length=200, blank=True)
    credential_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    
    date_obtained = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    
    is_visible = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-date_obtained', 'order']
    
    def __str__(self):
        return f"{self.name} - {self.issuing_organization}"