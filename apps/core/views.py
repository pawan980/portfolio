"""
Views for core app.
"""

from django.views.generic import TemplateView
from django.db import connection
from .models import Skill
from apps.projects.models import Project
from apps.experience.models import Experience
from apps.education.models import Education, Certification


class LandingView(TemplateView):
    """Focused landing page with key highlights."""
    template_name = 'pages/landing.html'
    
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
            # Featured projects (top 3-4)
            if self._table_exists('projects_project'):
                context['featured_projects'] = Project.objects.filter(
                    is_published=True, is_featured=True
                ).order_by('-created_at')[:4]
            else:
                context['featured_projects'] = []
            
            # Top skills (12-15 most important)
            if self._table_exists('core_skill'):
                skills = Skill.objects.filter(is_active=True).order_by('-proficiency')[:15]
                context['top_skills_by_category'] = {}
                for skill in skills:
                    category = skill.get_category_display()
                    if category not in context['top_skills_by_category']:
                        context['top_skills_by_category'][category] = []
                    context['top_skills_by_category'][category].append(skill)
            else:
                context['top_skills_by_category'] = {}
            
            # Recent experience (2-3 latest)
            if self._table_exists('experience_experience'):
                context['recent_experiences'] = Experience.objects.filter(
                    is_visible=True
                ).order_by('-start_date')[:3]
            else:
                context['recent_experiences'] = []
            
            # Quick stats
            context['stats'] = {
                'projects': Project.objects.filter(is_published=True).count() if self._table_exists('projects_project') else 0,
                'experience_years': self._calculate_experience_years(),
                'skills': Skill.objects.filter(is_active=True).count() if self._table_exists('core_skill') else 0,
                'certifications': Certification.objects.filter(is_visible=True).count() if self._table_exists('education_certification') else 0,
            }
        except Exception:
            context['featured_projects'] = []
            context['top_skills_by_category'] = {}
            context['recent_experiences'] = []
            context['stats'] = {'projects': 0, 'experience_years': 0, 'skills': 0, 'certifications': 0}
        
        return context
    
    def _calculate_experience_years(self):
        """Calculate total years of experience."""
        try:
            if not self._table_exists('experience_experience'):
                return 0
            from datetime import date
            from django.db.models import Min
            first_job = Experience.objects.filter(is_visible=True).aggregate(Min('start_date'))['start_date__min']
            if first_job:
                years = (date.today() - first_job).days / 365.25
                return int(years)
        except Exception:
            pass
        return 0


class AboutView(TemplateView):
    """Comprehensive about page with full details."""
    template_name = 'pages/about.html'
    
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
            # All skills grouped by category
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
            
            # All projects
            if self._table_exists('projects_project'):
                context['projects'] = Project.objects.filter(
                    is_published=True
                ).order_by('-created_at')
            else:
                context['projects'] = []
            
            # All experience
            if self._table_exists('experience_experience'):
                context['experiences'] = Experience.objects.filter(
                    is_visible=True
                ).order_by('-start_date')
            else:
                context['experiences'] = []
            
            # All education
            if self._table_exists('education_education'):
                context['education'] = Education.objects.filter(is_visible=True)
            else:
                context['education'] = []
            
            # All certifications
            if self._table_exists('education_certification'):
                context['certifications'] = Certification.objects.filter(
                    is_visible=True
                ).order_by('-date_obtained')
            else:
                context['certifications'] = []
            
            # All testimonials
            if self._table_exists('testimonials_testimonial'):
                from apps.testimonials.models import Testimonial
                context['testimonials'] = Testimonial.objects.all()
            else:
                context['testimonials'] = []
            
            # All blog posts
            if self._table_exists('blog_blogpost'):
                from apps.blog.models import BlogPost
                context['blog_posts'] = BlogPost.objects.filter(
                    is_published=True
                ).order_by('-published_date')
            else:
                context['blog_posts'] = []
        except Exception:
            context['skills_by_category'] = {}
            context['projects'] = []
            context['experiences'] = []
            context['education'] = []
            context['certifications'] = []
            context['testimonials'] = []
            context['blog_posts'] = []
        
        return context


# Keep for backward compatibility
HomeView = AboutView


def custom_404(request, exception):
    """Custom 404 error handler."""
    from django.shortcuts import render
    return render(request, '404.html', status=404)


def custom_500(request):
    """Custom 500 error handler."""
    from django.shortcuts import render
    return render(request, '500.html', status=500)