from django.db import models
#from users.models import CustomUser
from django.conf import settings

class Team(models.Model):
    title = models.CharField(max_length=70)
    founded_at = models.DateTimeField(null=True, blank=True)
    founder = models.CharField(max_length=200)
    history = models.TextField()
    emblem = models.ImageField(null=True,blank=True)
    banner = models.ImageField(null=True,blank=True)


    def __str__(self):
        return self.title


class Trophies(models.Model):
    title = models.CharField(max_length=90)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    won_at = models.DateField(null=True, blank=True)
    image = models.ImageField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title




class TeamPosts(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title        
