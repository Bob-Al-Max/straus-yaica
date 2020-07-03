from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.conf import settings

from .managers import CustomUserManager
from team.models import Team



class Contact(models.Model):
    user_from = models.ForeignKey('CustomUser',
                                  related_name='rel_from_set',
                                  on_delete=models.CASCADE)
    user_to = models.ForeignKey('CustomUser',
                                related_name='rel_to_set',
                                on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.user_from,
                                      self.user_to)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)
    profile_img = models.ImageField(null=True,blank=True)
    following = models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'id': self.id})
        





        
        
            

