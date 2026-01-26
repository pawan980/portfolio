from django.db import models


class Testimonial(models.Model):
    """Client testimonials and recommendations."""
    author = models.CharField(max_length=100, help_text="Client or colleague name")
    position = models.CharField(max_length=100, help_text="Job title")
    company = models.CharField(max_length=100, help_text="Company name")
    content = models.TextField(help_text="Testimonial text")
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True, help_text="Author photo")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5, help_text="Rating out of 5")
    is_featured = models.BooleanField(default=False, help_text="Show on homepage")
    order = models.IntegerField(default=0, help_text="Display order (lower first)")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
    
    def __str__(self):
        return f"{self.author} - {self.company}"
