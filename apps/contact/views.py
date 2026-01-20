"""
Views for contact app.
"""

from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


class ContactView(FormView):
    """Contact form view."""
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:contact')
    
    def form_valid(self, form):
        # Save submission
        submission = form.save(commit=False)
        submission.ip_address = self.get_client_ip()
        submission.user_agent = self.request.META.get('HTTP_USER_AGENT', '')[:500]
        submission.save()
        
        # Success message
        messages.success(self.request, 'Thank you! I\'ll get back to you soon.')
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