# Generated by Django 3.0.7 on 2020-06-28 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200627_2126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='follower',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterField(
            model_name='follower',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
