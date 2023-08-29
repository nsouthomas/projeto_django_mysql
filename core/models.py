from django.db import models
from django import forms
from stdimage.models import StdImageField
from django.db import models

from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now_add=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})

    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=244, verbose_name='Nome')
    email = models.EmailField(max_length=244, verbose_name='E-mail')
    assunto = models.CharField(max_length=244, verbose_name='Assunto')
    mensagem = models.TextField(verbose_name='Mensagem')

    def __str__(self):
        return self.nome