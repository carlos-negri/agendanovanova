# Generated by Django 5.2 on 2025-06-02 22:59

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='foto',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Foto'),
        ),
    ]
