# Generated by Django 5.2 on 2025-05-13 00:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_alter_produto_options'),
        ('servicos', '0004_alter_servico_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtosservico',
            name='produto',
            field=models.ForeignKey(help_text='Nome do produto utilizado', on_delete=django.db.models.deletion.CASCADE, related_name='produto', to='produtos.produto', verbose_name='Produto'),
        ),
        migrations.AlterField(
            model_name='produtosservico',
            name='quantidade',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Quantidade utilizada de produto', max_digits=5, verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='produtosservico',
            name='servico',
            field=models.ForeignKey(help_text='Nome do serviço realizado', on_delete=django.db.models.deletion.CASCADE, related_name='servico', to='servicos.servico', verbose_name='Serviço'),
        ),
    ]
