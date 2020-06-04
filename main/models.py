from django.db import models

class Main(models.Model):

    title = models.CharField(max_length=50)
    about = models.TextField(default="")
    logo = models.ImageField(null=True,blank=True)


    def __str__(self):
        return self.title
