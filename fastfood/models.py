from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('waiter', 'Waiter'),
        ('user', 'User'),
    ]
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, default='user')
    phone = models.CharField(max_length=13, unique=True)
    groups = None
    user_permissions = None

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class Food(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Food')
        verbose_name_plural = _('Foods')

    def __str__(self):
        return self.name

