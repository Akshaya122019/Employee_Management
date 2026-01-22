from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee

@receiver(post_save, sender=Employee)
def handle_employee_status_change(sender, instance, **kwargs):
    if instance.status == 'resigned':
        pass  # Only business logic, no user reference
