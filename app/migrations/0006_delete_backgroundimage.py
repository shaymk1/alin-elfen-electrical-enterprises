# Generated by Django 4.0.3 on 2022-03-30 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_services_svg_file'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BackgroundImage',
        ),
    ]