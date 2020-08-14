# Generated by Django 2.2 on 2020-08-12 20:32

import authentication.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=authentication.utils.upload_path),
        ),
        migrations.AlterField(
            model_name='profile',
            name='telephone_number',
            field=models.PositiveIntegerField(blank=True, max_length=10, null=True),
        ),
    ]
