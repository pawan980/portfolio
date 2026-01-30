from django.views.generic import CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Testimonial
from .forms import TestimonialSubmissionForm


class TestimonialSubmitView(CreateView):
    """View for public testimonial submission."""
    model = Testimonial
    form_class = TestimonialSubmissionForm
    template_name = 'testimonials/submit.html'
    success_url = reverse_lazy('testimonials:submit')
    
    def form_valid(self, form):
        # Set is_approved to False for moderation
        form.instance.is_approved = False
        response = super().form_valid(form)
        messages.success(
            self.request, 
            'Thank you for your testimonial! It will be reviewed and published soon.'
        )
        return response
    
    def form_invalid(self, form):
        messages.error(
            self.request,
            'There was an error submitting your testimonial. Please check the form and try again.'
        )
        return super().form_invalid(form)
