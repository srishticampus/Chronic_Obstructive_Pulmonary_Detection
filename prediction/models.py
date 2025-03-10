from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    image = models.ImageField(upload_to='profile_pics/')
    password = models.CharField(max_length=255)
    
    def clean(self):
        # Custom validation for age
        if self.age <= 0:
            raise ValidationError(_("Age must be a positive number."))

    def __str__(self):
        return self.username
