# Generated by Django 3.0.7 on 2020-06-30 13:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0011_auto_20200630_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='users_like',
        ),
        migrations.AddField(
            model_name='posts',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
