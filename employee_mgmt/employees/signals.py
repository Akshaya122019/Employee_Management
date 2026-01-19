from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee

@receiver(post_save, sender=Employee)
def handle_employee_status_change(sender, instance, **kwargs):
    if instance.user:
        if instance.status == 'resigned':
            if instance.user.is_active:
                instance.user.is_active = False
                instance.user.save()
        elif instance.status == 'active':
            if not instance.user.is_active:
                instance.user.is_active = True
                instance.user.save()
