from django.views.generic import ListView, DetailView
from django.db import connection
from .models import BlogPost


class BlogListView(ListView):
    model = BlogPost
    template_name = 'pages/blog/list.html'
    context_object_name = 'posts'
    paginate_by = 9
    
    def _table_exists(self, table_name):
        """Check if a database table exists using Django introspection."""
        try:
            table_names = connection.introspection.table_names()
            return table_name in table_names
        except Exception:
            return False
    
    def get_queryset(self):
        if not self._table_exists('blog_blogpost'):
            return BlogPost.objects.none()
        return BlogPost.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'pages/blog/detail.html'
    context_object_name = 'post'
    
    def _table_exists(self, table_name):
        """Check if a database table exists using Django introspection."""
        try:
            table_names = connection.introspection.table_names()
            return table_name in table_names
        except Exception:
            return False
    
    def get_queryset(self):
        if not self._table_exists('blog_blogpost'):
            return BlogPost.objects.none()
        return BlogPost.objects.filter(is_published=True)
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # Increment view count
        obj.views += 1
        obj.save(update_fields=['views'])
        return obj
