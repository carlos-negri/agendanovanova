# Generated by Django 5.2 on 2025-06-02 22:26

import django.db.models.functions.text
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do fornecedor', max_length=70, verbose_name='Nome')),
                ('cnpj', models.CharField(help_text='CNPJ do fornecedor', max_length=18, unique=True, verbose_name='Cnpj')),
                ('fone', models.CharField(help_text='Fone do fornecedor', max_length=15, verbose_name='Fone')),
            ],
            options={
                'verbose_name': 'Fornecedor',
                'verbose_name_plural': 'Fornecedores',
                'ordering': [django.db.models.functions.text.Upper('nome')],
            },
        ),
    ]
