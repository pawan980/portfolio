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
        
        queryset = Project.objects.all()
        
        # Filter by category if provided
        category = self.request.GET.get('category')
        if category and category != 'all':
            # Filter projects that have this category in their categories field
            queryset = queryset.filter(categories__icontains=category)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_category'] = self.request.GET.get('category', 'all')
        context['categories'] = Project.CATEGORY_CHOICES
        return context


class ProjectDetailView(DetailView):
    """Display single project detail."""
    model = Project
    template_name = 'pages/projects/detail.html'
    context_object_name = 'project'
    
    def get_queryset(self):
        return Project.objects.all()