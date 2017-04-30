from django.contrib import admin
from .models import Post, User, DadosPagamento, DadosPessoais

# Register your models here.
admin.site.register(Post)
admin.site.register(User)
admin.site.register(DadosPessoais)
admin.site.register(DadosPagamento)