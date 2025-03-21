# Generated by Django 5.1.2 on 2025-03-17 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0002_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='doctor_images/'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='name',
            field=models.CharField(default='Unknown Doctor', max_length=255),
        ),
    ]
