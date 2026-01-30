from django.urls import path
from .views import TestimonialSubmitView

app_name = 'testimonials'

urlpatterns = [
    path('submit/', TestimonialSubmitView.as_view(), name='submit'),
]
