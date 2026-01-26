from django.core.exceptions import ValidationError
from PIL import Image

def validate_jpg_image(image):
    max_size = 2 * 1024 * 1024 

    if image.size > max_size:
        raise ValidationError("Image size must be under 2MB.")

    allowed_formats = ['JPEG', 'PNG', 'WEBP']

    try:
        img = Image.open(image)
        img.verify() 

        image.seek(0)
        img = Image.open(image)

        if img.format not in allowed_formats:
            raise ValidationError("Only JPG, PNG, or WEBP images are allowed.")

    except Exception:
        raise ValidationError("Invalid or corrupted image file.")
