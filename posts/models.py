from django.db import models
from users.models import CustomUser
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save
from .utils import unique_slug_generator





class Posts(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='likes')
    content = models.TextField()
    image = models.ImageField(upload_to="posts/%Y/%m/%d", null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    #rewriting save method for automaticly saving slugs
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title) + str(self.pk)
    #     super(Posts, self).save(*args, **kwargs)    


    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Posts)        



                






     
