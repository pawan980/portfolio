"""
Views for core app.
"""

from django.views.generic import TemplateView
from django.db import connection
from .models import Skill
from apps.projects.models import Project
from apps.experience.models import Experience
from apps.education.models import Education, Certification


class HomeView(TemplateView):
    """Main homepage displaying all sections."""
    template_name = 'pages/home.html'
    
    def _table_exists(self, table_name):
        """Check if a database table exists using Django introspection."""
        try:
            table_names = connection.introspection.table_names()
            return table_name in table_names
        except Exception:
            return False
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        try:
            # Skills grouped by category
            if self._table_exists('core_skill'):
                skills = Skill.objects.filter(is_active=True)
                context['skills_by_category'] = {}
                for skill in skills:
                    category = skill.get_category_display()
                    if category not in context['skills_by_category']:
                        context['skills_by_category'][category] = []
                    context['skills_by_category'][category].append(skill)
            else:
                context['skills_by_category'] = {}
            
            # Featured projects
            if self._table_exists('projects_project'):
                context['projects'] = Project.objects.filter(
                    is_published=True, is_featured=True
                ).order_by('-created_at')[:6]
            else:
                context['projects'] = []
            
            # Recent experience
            if self._table_exists('experience_experience'):
                context['experiences'] = Experience.objects.filter(
                    is_visible=True
                ).order_by('-start_date')[:5]
            else:
                context['experiences'] = []
            
            # Education
            if self._table_exists('education_education'):
                context['education'] = Education.objects.filter(is_visible=True)
            else:
                context['education'] = []
            
            # Certifications
            if self._table_exists('education_certification'):
                context['certifications'] = Certification.objects.filter(
                    is_visible=True
                ).order_by('-date_obtained')[:6]
            else:
                context['certifications'] = []
        except Exception:
            # If anything fails, return empty collections
            context['skills_by_category'] = {}
            context['projects'] = []
            context['experiences'] = []
            context['education'] = []
            context['certifications'] = []
        
        return context


def custom_404(request, exception):
    """Custom 404 error handler."""
    from django.shortcuts import render
    return render(request, '404.html', status=404)


def custom_500(request):
    """Custom 500 error handler."""
    from django.shortcuts import render
    return render(request, '500.html', status=500)