"""
Image optimization utilities.
"""
import os
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile


class ImageOptimizer:
    """Optimize images by resizing and compressing."""
    
    # Maximum dimensions
    MAX_WIDTH = 1920
    MAX_HEIGHT = 1080
    
    # Thumbnail sizes
    THUMBNAIL_SIZES = {
        'small': (480, 480),
        'medium': (768, 768),
        'large': (1200, 1200),
    }
    
    # Quality settings
    JPEG_QUALITY = 85
    WEBP_QUALITY = 85
    
    @classmethod
    def optimize_image(cls, image_field, max_width=None, max_height=None):
        """
        Optimize an image by resizing and compressing.
        
        Args:
            image_field: Django ImageField
            max_width: Maximum width (default: MAX_WIDTH)
            max_height: Maximum height (default: MAX_HEIGHT)
            
        Returns:
            Optimized image as ContentFile
        """
        if not image_field:
            return None
        
        max_width = max_width or cls.MAX_WIDTH
        max_height = max_height or cls.MAX_HEIGHT
        
        try:
            # Open image
            img = Image.open(image_field)
            
            # Convert RGBA to RGB if necessary
            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            
            # Resize if needed
            if img.width > max_width or img.height > max_height:
                img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
            
            # Save optimized image
            output = BytesIO()
            img_format = 'JPEG'
            
            # Determine format from filename
            filename = image_field.name
            if filename.lower().endswith('.png'):
                img_format = 'PNG'
            elif filename.lower().endswith('.webp'):
                img_format = 'WEBP'
            
            # Save with optimization
            if img_format == 'JPEG':
                img.save(output, format=img_format, quality=cls.JPEG_QUALITY, optimize=True)
            elif img_format == 'WEBP':
                img.save(output, format=img_format, quality=cls.WEBP_QUALITY)
            else:
                img.save(output, format=img_format, optimize=True)
            
            output.seek(0)
            
            # Get filename
            name = os.path.basename(filename)
            
            return ContentFile(output.read(), name=name)
            
        except Exception as e:
            print(f"Error optimizing image: {e}")
            return None
    
    @classmethod
    def create_thumbnail(cls, image_field, size='medium'):
        """
        Create a thumbnail of specified size.
        
        Args:
            image_field: Django ImageField
            size: 'small', 'medium', or 'large'
            
        Returns:
            Thumbnail as ContentFile
        """
        if not image_field or size not in cls.THUMBNAIL_SIZES:
            return None
        
        try:
            img = Image.open(image_field)
            
            # Convert RGBA to RGB
            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            
            # Create thumbnail
            img.thumbnail(cls.THUMBNAIL_SIZES[size], Image.Resampling.LANCZOS)
            
            # Save
            output = BytesIO()
            img.save(output, format='JPEG', quality=cls.JPEG_QUALITY, optimize=True)
            output.seek(0)
            
            # Generate filename
            filename = os.path.basename(image_field.name)
            name, ext = os.path.splitext(filename)
            thumb_name = f"{name}_{size}{ext}"
            
            return ContentFile(output.read(), name=thumb_name)
            
        except Exception as e:
            print(f"Error creating thumbnail: {e}")
            return None
