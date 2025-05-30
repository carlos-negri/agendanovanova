from django.db import models
from django.db.models.functions import Upper


class Fornecedor(models.Model):
        nome = models.CharField('Nome', max_length=70, help_text='Nome do fornecedor')
        cnpj = models.CharField('Cnpj', max_length=18, help_text='CNPJ do fornecedor', unique=True)
        fone = models.CharField('Fone', max_length=15, help_text='Fone do fornecedor')


        class Meta:
                verbose_name = 'Fornecedor'
                verbose_name_plural = 'Fornecedores'
                ordering = [Upper('nome')]


        def __str__(self):
            return self.nome




