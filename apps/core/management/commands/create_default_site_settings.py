"""
Management command to create default SiteSettings if none exists.
"""
from django.core.management.base import BaseCommand
from apps.core.models import SiteSettings

class Command(BaseCommand):
    help = 'Creates default SiteSettings if none exists'

    def handle(self, *args, **options):
        if SiteSettings.objects.exists():
            self.stdout.write(self.style.SUCCESS('SiteSettings already exists'))
            return

        SiteSettings.objects.create(
            full_name='Your Name',
            tagline='Full Stack Developer',
            bio='Welcome to my portfolio',
            email='your@email.com',
            phone='+1234567890',
            location='Your City',
            meta_description='Portfolio website',
            meta_keywords='portfolio, developer',
        )
        
        self.stdout.write(self.style.SUCCESS('Default SiteSettings created'))
