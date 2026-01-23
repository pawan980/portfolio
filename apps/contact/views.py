"""
Views for contact app.
"""

from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.db import connection
from .forms import ContactForm


class ContactView(FormView):
    """Contact form view."""
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:contact')
    
    def _table_exists(self, table_name):
        """Check if a database table exists using Django introspection."""
        try:
            table_names = connection.introspection.table_names()
            return table_name in table_names
        except Exception:
            return False
    
    def form_valid(self, form):
        try:
            # Only save if the table exists
            if self._table_exists('contact_contactsubmission'):
                # Save submission
                submission = form.save(commit=False)
                submission.ip_address = self.get_client_ip()
                submission.user_agent = self.request.META.get('HTTP_USER_AGENT', '')[:500]
                submission.save()
            
            # Success message
            messages.success(self.request, 'Thank you! I\'ll get back to you soon.')
        except Exception as e:
            messages.error(self.request, 'There was an error processing your request.')
        
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Please check the form and try again.')
        return super().form_invalid(form)
    
    def get_client_ip(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip