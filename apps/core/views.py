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
            # Featured projects (projects marked to show on about page, top 4)
            if self._table_exists('projects_project'):
                context['featured_projects'] = Project.objects.filter(
                    show_on_about_page=True
                ).order_by('order', '-created_at')[:4]
            else:
                context['featured_projects'] = []
            
            # Featured skills by category
            if self._table_exists('core_skill'):
                skills = Skill.objects.filter(is_active=True, is_featured=True).order_by('order', 'name')
                context['top_skills_by_category'] = {}
                for skill in skills:
                    category = skill.get_category_display()
                    if category not in context['top_skills_by_category']:
                        context['top_skills_by_category'][category] = []
                    context['top_skills_by_category'][category].append(skill)
            else:
                context['top_skills_by_category'] = {}
            
            # Featured certifications (top 4)
            if self._table_exists('education_certification'):
                context['featured_certifications'] = Certification.objects.filter(
                    is_visible=True
                ).order_by('order', '-date_obtained')[:4]
            else:
                context['featured_certifications'] = []
                
        except Exception:
            context['featured_projects'] = []
            context['top_skills_by_category'] = {}
            context['featured_certifications'] = []
        
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
            # All skills grouped hierarchically for cyberpunk design
            if self._table_exists('core_skill'):
                from collections import OrderedDict
                skills = Skill.objects.filter(is_active=True)
                
                #Define category order for numbered cards (01-06)
                category_order = [
                    'compute',
                    'data',
                    'platform',
                    'devops',
                    'observability',
                    'architecture',
                ]
                
                # Group skills by category and subcategory
                skills_hierarchy = {}
                for skill in skills:
                    category = skill.category
                    if category not in skills_hierarchy:
                        skills_hierarchy[category] = {}
                    
                    subcategory = skill.subcategory
                    if subcategory not in skills_hierarchy[category]:
                        skills_hierarchy[category][subcategory] = []
                    
                    skills_hierarchy[category][subcategory].append(skill)
                
                # Build ordered structure with metadata
                context['skills_categories'] = []
                for idx, cat_key in enumerate(category_order, 1):
                    if cat_key in skills_hierarchy:
                        context['skills_categories'].append({
                            'number': f'{idx:02d}',  # 01, 02, 03, etc.
                            'key': cat_key,
                            'name': dict(Skill.CATEGORY_CHOICES)[cat_key],
                            'description': Skill.CATEGORY_DESCRIPTIONS[cat_key],
                            'icon': Skill.CATEGORY_ICONS[cat_key],
                            'subcategories': skills_hierarchy[cat_key]
                        })
            else:
                context['skills_categories'] = []
            
            # Projects marked to show on about page
            if self._table_exists('projects_project'):
                context['projects'] = Project.objects.filter(
                    show_on_about_page=True
                ).order_by('order', '-created_at')
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
            
            # Approved testimonials
            if self._table_exists('testimonials_testimonial'):
                from apps.testimonials.models import Testimonial
                context['testimonials'] = Testimonial.objects.filter(is_approved=True).order_by('order', '-created_at')
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