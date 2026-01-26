"""
URL configuration for analytics app.
"""
from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('resume/download/', views.ResumeDownloadView.as_view(), name='resume_download'),
]
