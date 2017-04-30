from django.shortcuts import render
from .models import Post, DadosPessoais, User, DadosPagamento
from .serializer import PostSerializer, DadosPessoaisSerializer, DadosPagamentoSerializer, UserSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

def post_exibir(request):
    texto =  Post.objects.all()
    context = {'texto':texto}

    return render(request, '', context)

class PostListView(APIView):
    serializer_class = PostSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Post.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)

class PostView(APIView):

    def get(self, request, pk, format=None):
        user = Post.objects.get(pk=pk)
        serializer = PostSerializer(user)
        return Response(serializer.data)

class DadosPessoaisListView(APIView):
    serializer_class = DadosPessoaisSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(DadosPessoais.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)

class DadosPagamentoListView(APIView):
    serializer_class = DadosPagamentoSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(DadosPagamento.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)

class UserListView(APIView):
    serializer_class = UserSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(User.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)