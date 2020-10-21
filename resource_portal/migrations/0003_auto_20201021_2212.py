# Generated by Django 3.0.8 on 2020-10-21 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource_portal', '0002_resource_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='file',
            field=models.FileField(upload_to='resource_portal/Files/'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='thumbnail',
            field=models.ImageField(upload_to='resource_portal/thumbnail/'),
        ),
    ]
