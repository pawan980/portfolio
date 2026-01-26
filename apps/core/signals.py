"""
Signal handlers for automatic image optimization.
"""
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import SiteSettings
from .utils.image_optimizer import ImageOptimizer


@receiver(pre_save, sender=SiteSettings)
def optimize_site_images(sender, instance, **kwargs):
    """Optimize profile image when SiteSettings is saved."""
    if instance.profile_image:
        try:
            # Check if this is a new upload or changed image
            if instance.pk:
                try:
                    old_instance = SiteSettings.objects.get(pk=instance.pk)
                    if old_instance.profile_image == instance.profile_image:
                        return  # Image hasn't changed
                except SiteSettings.DoesNotExist:
                    pass
            
            # Optimize the image
            optimized = ImageOptimizer.optimize_image(
                instance.profile_image,
                max_width=500,  # Profile images don't need to be huge
                max_height=500
            )
            
            if optimized:
                instance.profile_image.save(
                    optimized.name,
                    optimized,
                    save=False
                )
        except Exception as e:
            print(f"Error optimizing profile image: {e}")
