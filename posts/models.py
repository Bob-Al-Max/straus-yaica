from django.db import models
from users.models import CustomUser
from django.conf import settings
from django.urls import reverse

class Posts(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='likes')
    content = models.TextField()
    image = models.ImageField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})


    def get_like_url(self):
        return reverse("like-toggle", kwargs={"slug": self.slug})


    def get_api_like_url(self):
        return reverse("like-api-toggle", kwargs={"slug": self.slug})            






     
