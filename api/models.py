from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

DESIGNATION_CHOICES = [
        ('SuperAdmin', 'SuperAdmin'),
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    ]

# custom user model
class User(AbstractUser):
    username = models.CharField(_('username'), max_length=30, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    title = models.CharField(max_length=15, choices=DESIGNATION_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return "{}".format(self.email)
