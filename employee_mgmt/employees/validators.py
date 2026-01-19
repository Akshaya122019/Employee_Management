from django.core.exceptions import ValidationError
from PIL import Image

def validate_jpg_image(image):

    if not image.name.lower().endswith(('.jpg', '.jpeg')):
        raise ValidationError('Only JPG images are allowed.')


    max_size = 2 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError('Image size must be under 2MB.')

  
    try:
        img = Image.open(image)
        img.verify()
        if img.format not in ['JPEG']:
            raise ValidationError('Invalid image format.')
    except Exception:
        raise ValidationError('Invalid or corrupted image file.')
