# Generated by Django 4.1.13 on 2025-04-18 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kbm', '0010_relatedimage_dept'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relatedimage',
            name='Dept',
        ),
    ]
