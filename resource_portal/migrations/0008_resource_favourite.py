# Generated by Django 3.0.8 on 2020-11-02 10:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resource_portal', '0007_resource_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='favourite',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
