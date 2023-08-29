# Generated by Django 4.2.4 on 2023-08-29 08:49

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado', models.DateField(auto_now_add=True, verbose_name='Data de Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('estoque', models.IntegerField(verbose_name='Estoque')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to='produtos', variations={'thumb': (124, 124)}, verbose_name='Imagem')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='contato',
            name='assunto',
            field=models.CharField(default='', max_length=244, verbose_name='Assunto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contato',
            name='email',
            field=models.EmailField(default='', max_length=244, verbose_name='E-mail'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contato',
            name='mensagem',
            field=models.TextField(default='', verbose_name='Mensagem'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contato',
            name='nome',
            field=models.CharField(default='', max_length=244, verbose_name='Nome'),
            preserve_default=False,
        ),
    ]
