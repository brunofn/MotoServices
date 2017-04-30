# coding=utf-8

from .models import Post, DadosPessoais, DadosPagamento, User
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        depth = 1
        fields = ['id','author','title','text']

class DadosPessoaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosPessoais
        depth = 1
        fields = ['nome', 'data_nascimento', 'telefone', 'cpf', 'login', 'cnh']

class DadosPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosPagamento
        depth = 1
        fields = ['user', 'validade', 'cod_seguranca', 'numero_cartao']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        depth = 1
        fields = ['email', 'senha']