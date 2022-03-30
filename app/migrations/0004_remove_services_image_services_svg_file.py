# Generated by Django 4.0.3 on 2022-03-30 10:33

import app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_services_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='image',
        ),
        migrations.AddField(
            model_name='services',
            name='svg_file',
            field=models.FileField(blank=True, upload_to='assets/', validators=[app.validators.validate_file_extension]),
        ),
    ]