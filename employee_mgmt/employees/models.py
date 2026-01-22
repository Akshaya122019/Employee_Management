from django.db import models
from django.conf import settings
from .validators import validate_jpg_image


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Team(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='teams'
    )
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('company', 'name')

    def __str__(self):
        return f"{self.name} ({self.company.name})"
    

class Employee(models.Model):

    STATUS_CHOICES = (
        ('active', 'Active'),
        ('resigned', 'Resigned'),
    )

    BLOOD_GROUP_CHOICES = (
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='employees'
    )

    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='employees'
    )

    name = models.CharField(max_length=100)
    identity_card_id = models.CharField(max_length=50, unique=True)

    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True,blank=True,null=True)
    role = models.CharField(max_length=100)

    photo = models.ImageField(
        upload_to='employee_photos/',
        blank=True,
        null=True,
        validators=[validate_jpg_image]
    )

    blood_group = models.CharField(
        max_length=5,
        choices=BLOOD_GROUP_CHOICES
    )

    date_of_joining = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active'
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_employees'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"
