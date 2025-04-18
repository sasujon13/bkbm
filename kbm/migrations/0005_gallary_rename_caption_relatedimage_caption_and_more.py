# Generated by Django 4.1.13 on 2025-04-17 15:02

from django.db import migrations, models
import django.db.models.deletion
import kbm.models


class Migration(migrations.Migration):

    dependencies = [
        ('kbm', '0004_departments_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Caption', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='relatedimage',
            old_name='caption',
            new_name='Caption',
        ),
        migrations.RemoveField(
            model_name='relatedimage',
            name='image',
        ),
        migrations.AddField(
            model_name='relatedimage',
            name='Dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kbm.dept'),
        ),
        migrations.AddField(
            model_name='relatedimage',
            name='Img',
            field=models.ImageField(blank=True, null=True, upload_to=kbm.models.upload_to_dept_folder),
        ),
    ]
