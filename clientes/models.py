from cloudinary.models import CloudinaryField
from django.db import models
from django.db.models.functions import Upper

from stdimage import StdImageField


class Pessoa(models.Model):
    nome = models.CharField(max_length=50, help_text='Nome completo')
    fone = models.CharField('Telefone', max_length=15, help_text='Número de telefone')
    email = models.EmailField('E-mail', max_length=100, help_text='Endereço de e-mail', unique=True)
    foto = CloudinaryField('Foto', null=True, blank=True)


    class Meta:
        abstract = True


    def __str__(self):
        return self.nome


class Cliente(Pessoa):
    endereco = models.CharField('Endereço', max_length=100, help_text='Endereço completo')


    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = [Upper('nome')]


    def __str__(self):
        return  super().nome