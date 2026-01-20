"""
Views for core app.
"""

from django.views.generic import TemplateView
from .models import Skill
from apps.projects.models import Project
from apps.experience.models import Experience
from apps.education.models import Education, Certification


class HomeView(TemplateView):
    """Main homepage displaying all sections."""
    template_name = 'pages/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Skills grouped by category
        skills = Skill.objects.filter(is_active=True)
        context['skills_by_category'] = {}
        for skill in skills:
            category = skill.get_category_display()
            if category not in context['skills_by_category']:
                context['skills_by_category'][category] = []
            context['skills_by_category'][category].append(skill)
        
        # Featured projects
        context['projects'] = Project.objects.filter(
            is_published=True, is_featured=True
        ).order_by('-created_at')[:6]
        
        # Recent experience
        context['experiences'] = Experience.objects.filter(
            is_visible=True
        ).order_by('-start_date')[:5]
        
        # Education
        context['education'] = Education.objects.filter(is_visible=True)
        
        # Certifications
        context['certifications'] = Certification.objects.filter(
            is_visible=True
        ).order_by('-date_obtained')[:6]
        
        return context