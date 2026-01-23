"""
Views for projects app.
"""

from django.views.generic import ListView, DetailView
from django.db import connection
from .models import Project


class ProjectListView(ListView):
    """Display all published projects."""
    model = Project
    template_name = 'pages/projects/list.html'
    context_object_name = 'projects'
    paginate_by = 12
    
    def _table_exists(self, table_name):
        """Check if a database table exists using Django introspection."""
        try:
            table_names = connection.introspection.table_names()
            return table_name in table_names
        except Exception:
            return False
    
    def get_queryset(self):
        if not self._table_exists('projects_project'):
            return Project.objects.none()
        return Project.objects.filter(is_published=True)


class ProjectDetailView(DetailView):
    """Display single project detail."""
    model = Project
    template_name = 'pages/projects/detail.html'
    context_object_name = 'project'
    
    def get_queryset(self):
        return Project.objects.filter(is_published=True)