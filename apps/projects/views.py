"""
Views for projects app.
"""

from django.views.generic import ListView, DetailView
from .models import Project


class ProjectListView(ListView):
    """Display all published projects."""
    model = Project
    template_name = 'pages/projects/list.html'
    context_object_name = 'projects'
    paginate_by = 12
    
    def get_queryset(self):
        return Project.objects.filter(is_published=True)


class ProjectDetailView(DetailView):
    """Display single project detail."""
    model = Project
    template_name = 'pages/projects/detail.html'
    context_object_name = 'project'
    
    def get_queryset(self):
        return Project.objects.filter(is_published=True)