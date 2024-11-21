from django.shortcuts import render, redirect # type: ignore
from .forms import ProdutoForm
from rest_framework import generics # type: ignore
from .models import Produto
from .serializers import ProdutoSerializer
from rest_framework.permissions import IsAuthenticated # type: ignore
from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore

class ExemploView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Você está autenticado!"})

class ProdutoListCreateView(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProdutoRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

def produto_new(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('produto_success')  
    else:
        form = ProdutoForm()
    return render(request, 'produto_new.html', {'form': form})

def produto_success(request):
    return render(request, 'produto_success.html')