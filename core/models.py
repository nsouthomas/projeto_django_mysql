from django.db import models
from django import forms

class Contato(models.Model):
    nome = forms.CharField (max_length= 244, label = 'Nome')
    email = forms.EmailField (max_length= 244, label = 'E-mail')
    assunto = forms.CharField (max_length= 244, label = 'Assunto')
    mensagem = forms.CharField (max_length= 244, label = 'Mensagem', widget= forms.Textarea())

    def __str__(self):
        return self.nome