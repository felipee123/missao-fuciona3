from rest_framework import serializers # type: ignore
from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'preco', 'validade']