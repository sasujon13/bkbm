# Generated by Django 4.1.13 on 2025-04-16 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kbm', '0003_remove_departments_titlestaff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='departments',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/depts'),
        ),
    ]
