from django import forms
from .models import Contato
from django.core.mail.message import EmailMessage

from .models import Produto

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = "__all__"

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE=mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject= 'E-mail enviado pelo sistema Django',
            body= conteudo,
            from_email='contato@seudominio.com.br',
            to= ['contato.django@teste.com'],
            headers={'Reply-to': email}
        )
        mail.send

class ProdutoModelForm(forms.ModelForm):    
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']