# Generated by Django 4.1.13 on 2025-04-18 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kbm', '0006_remove_relatedimage_dept_gallary_dept'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallary',
            name='Caption',
        ),
    ]
