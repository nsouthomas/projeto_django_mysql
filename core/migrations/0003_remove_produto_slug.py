# Generated by Django 4.2.4 on 2023-08-29 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_produto_contato_assunto_contato_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='slug',
        ),
    ]