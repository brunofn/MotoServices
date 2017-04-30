from django.db import models

# Create your models here.
from django.utils import timezone

class Post(models.Model):
    author = models.TextField()
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class User(models.Model):
    email = models.EmailField(verbose_name='Email', primary_key=True)
    senha = models.CharField(max_length=8)

    def __str__(self):
        return self.email

class DadosPessoais(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    data_nascimento = models.CharField(max_length=10, default='01/01/01', verbose_name='Data de Nascimento')
    telefone = models.CharField(max_length=14, verbose_name='Telefone')
    cpf = models.CharField(max_length=11, verbose_name='CPF', primary_key=True)

    login = models.ForeignKey(User)

    cnh = models.CharField(max_length=11, verbose_name='CNH')

    def __str__(self):
        return self.nome

class DadosPagamento(models.Model):
    user = models.ForeignKey(DadosPessoais)
    validade = models.CharField(max_length=5, verbose_name='Validade cartao')
    cod_seguranca = models.CharField(max_length=3, verbose_name='codigo de seguranca')
    numero_cartao = models.CharField(max_length=16, verbose_name='Cartao')

    def __srt__(self):
        return self.user
