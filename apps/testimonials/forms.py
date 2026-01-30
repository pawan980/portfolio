from django import forms
from .models import Testimonial


class TestimonialSubmissionForm(forms.ModelForm):
    """Form for public testimonial submission."""
    
    class Meta:
        model = Testimonial
        fields = ['author', 'position', 'company', 'content', 'linkedin_url', 'rating', 'photo']
        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-black/50 border border-cyan-500/30 rounded-lg text-cyan-100 placeholder-gray-500 focus:border-cyan-500 focus:outline-none focus:ring-2 focus:ring-cyan-500/50 transition-all duration-300',
                'placeholder': 'Your full name'
            }),
            'position': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-black/50 border border-cyan-500/30 rounded-lg text-cyan-100 placeholder-gray-500 focus:border-cyan-500 focus:outline-none focus:ring-2 focus:ring-cyan-500/50 transition-all duration-300',
                'placeholder': 'Your job title'
            }),
            'company': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-black/50 border border-cyan-500/30 rounded-lg text-cyan-100 placeholder-gray-500 focus:border-cyan-500 focus:outline-none focus:ring-2 focus:ring-cyan-500/50 transition-all duration-300',
                'placeholder': 'Your company'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 bg-black/50 border border-cyan-500/30 rounded-lg text-cyan-100 placeholder-gray-500 focus:border-cyan-500 focus:outline-none focus:ring-2 focus:ring-cyan-500/50 transition-all duration-300 resize-vertical',
                'placeholder': 'Share your experience working with me...',
                'rows': 5
            }),
            'linkedin_url': forms.URLInput(attrs={
                'class': 'w-full px-4 py-3 bg-black/50 border border-cyan-500/30 rounded-lg text-cyan-100 placeholder-gray-500 focus:border-cyan-500 focus:outline-none focus:ring-2 focus:ring-cyan-500/50 transition-all duration-300',
                'placeholder': 'https://linkedin.com/in/yourprofile (optional)'
            }),
            'rating': forms.Select(attrs={
                'class': 'w-full px-4 py-3 bg-black/50 border border-cyan-500/30 rounded-lg text-cyan-100 focus:border-cyan-500 focus:outline-none focus:ring-2 focus:ring-cyan-500/50 transition-all duration-300'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'w-full px-4 py-3 bg-black/50 border border-cyan-500/30 rounded-lg text-cyan-100 focus:border-cyan-500 focus:outline-none focus:ring-2 focus:ring-cyan-500/50 transition-all duration-300'
            })
        }
        labels = {
            'author': 'Your Name',
            'position': 'Job Title',
            'company': 'Company',
            'content': 'Your Testimonial',
            'linkedin_url': 'LinkedIn Profile (Optional)',
            'rating': 'Rating',
            'photo': 'Your Photo (Optional)'
        }
        help_texts = {
            'content': 'Tell us about your experience working together',
            'linkedin_url': 'Help us verify your identity',
            'photo': 'A professional photo to display with your testimonial'
        }
