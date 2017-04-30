# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 22:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20170409_2339'),
    ]

    operations = [
        migrations.CreateModel(
            name='DadosPagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validade', models.CharField(max_length=5, verbose_name='Validade cartao')),
                ('cod_seguranca', models.CharField(max_length=3, verbose_name='codigo de seguranca')),
                ('numero_cartao', models.CharField(max_length=16, verbose_name='Cartao')),
            ],
        ),
        migrations.CreateModel(
            name='DadosPessoais',
            fields=[
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('data_nascimento', models.CharField(default='01/01/01', max_length=10, verbose_name='Data de Nascimento')),
                ('telefone', models.CharField(max_length=14, verbose_name='Telefone')),
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='CPF')),
                ('cnh', models.CharField(max_length=11, verbose_name='CNH')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, verbose_name='Email')),
                ('senha', models.CharField(max_length=8)),
            ],
        ),
        migrations.AddField(
            model_name='dadospessoais',
            name='login',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.User'),
        ),
        migrations.AddField(
            model_name='dadospagamento',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.DadosPessoais'),
        ),
    ]