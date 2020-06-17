from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from .managers import CustomUserManager
from team.models import Team


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)
    profile_img = models.ImageField(null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'id': self.id})     
